"""Regression checks for the film's editorial and story continuity contracts."""
import copy
import ast
import json
import unittest
from pathlib import Path

import build_prompts_v3 as film


class FilmContinuityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = json.loads((film.BASE_DIR/'PHAN_CANH_V3.json').read_text())
        cls.shots = film.normalize(cls.plan)
        cls.index = {c['id']:c for c in cls.shots}

    def test_whole_film_is_valid(self):
        film.validate(self.plan,self.shots)
        self.assertEqual(len(self.shots),360)
        self.assertEqual(len(list(zip(self.shots,self.shots[1:]))),359)

    def test_continuation_uses_exact_end_without_repeating_action(self):
        for a,b in zip(self.shots,self.shots[1:]):
            if b['transition']=='CONTINUE':
                self.assertEqual(b['start_frame'],a['end_frame'],b['id'])
                self.assertEqual((b['location'],b['camera'],b['story_time']),
                                 (a['location'],a['camera'],a['story_time']),b['id'])
                self.assertNotEqual(b['action'],a['action'],b['id'])

    def test_location_change_cannot_masquerade_as_continuation(self):
        altered=copy.deepcopy(self.shots)
        shot=next(c for c in altered if c['transition']=='CONTINUE')
        shot['location']='CROSSROAD'
        with self.assertRaisesRegex(ValueError,'changes location/camera/time'):
            film.validate(self.plan,altered)

    def test_visual_state_regressions_are_rejected(self):
        altered=copy.deepcopy(self.shots)
        next(c for c in altered if c['id']=='51.5')['characters'].append('HA_N')
        with self.assertRaisesRegex(ValueError,'clean clothes before station change'):
            film.validate(self.plan,altered)
        altered=copy.deepcopy(self.shots)
        next(c for c in altered if c['id']=='11.5')['props'].append('WATCH_OPEN')
        with self.assertRaisesRegex(ValueError,'first open-watch shot'):
            film.validate(self.plan,altered)

    def test_replayed_action_and_injected_spoken_tags_are_rejected(self):
        altered=copy.deepcopy(self.shots)
        altered[1]['action']=altered[0]['action']
        with self.assertRaisesRegex(ValueError,'action repeats'):
            film.validate(self.plan,altered)
        altered=copy.deepcopy(self.shots)
        next(c for c in altered if c['dialogue'])['dialogue'][0]['text']+=' @Son'
        with self.assertRaisesRegex(ValueError,'injected tag/quote'):
            film.validate(self.plan,altered)

    def test_generator_mode_matches_actual_edit_type(self):
        for i,c in enumerate(self.shots):
            text=film.render_prompt(self.plan,c,self.shots[i-1] if i else None,
                                    self.shots[i+1] if i<359 else None)
            self.assertEqual(text.startswith('Continue'),c['transition']=='CONTINUE',c['id'])
            self.assertEqual(text.startswith('[FORMAT]'),c['transition']!='CONTINUE',c['id'])
            self.assertNotIn('2.39:1',text)
            self.assertNotIn('0.5s',text)
            self.assertNotIn('one slow-motion beat',text)
            self.assertNotIn('[project LIST]',text)

    def test_all_handoffs_are_exported_and_output_is_deterministic(self):
        out=film.outputs(self.plan,self.shots)
        self.assertEqual(out,film.outputs(self.plan,film.normalize(self.plan)))
        self.assertEqual(len([p for p in out if '/clip-' in p]),360)
        table=out['BANG_NOI_CLIP.md']
        for a,b in zip(self.shots,self.shots[1:]):
            self.assertIn(f"[{a['id']}]({film.ref(a)}) → [{b['id']}]({film.ref(b)})",table)
        self.assertEqual(len(out),486 if film.edition(self.plan)=='3.1' else 485)
        manifest=json.loads(out['RENDER_MANIFEST_V3.json'])
        self.assertEqual(len(manifest['clips']),360)

    def test_detailed_edition_cannot_silently_omit_directing(self):
        incomplete=copy.deepcopy(self.plan)
        incomplete['editorial_revision']='3.1'
        incomplete['scenes'][0]['clips'][0].pop('cinematic',None)
        with self.assertRaisesRegex(ValueError,'incomplete specific directing detail'):
            film.validate(incomplete,film.normalize(incomplete))

    def test_scene_and_shot_details_are_exported_without_new_dialogue(self):
        if film.edition(self.plan)!='3.1':
            self.skipTest('Detail pass has not been merged yet')
        for i,c in enumerate(self.shots):
            prompt=film.render_prompt(self.plan,c,self.shots[i-1] if i else None,
                                      self.shots[i+1] if i<359 else None)
            for field in film.DETAIL_FIELDS:
                self.assertIn(c['cinematic'][field],prompt,(c['id'],field))
            dialogue=prompt.split('[DIALOGUE]\n',1)[1].split('\n[PROPS]',1)[0]
            self.assertNotIn(c['cinematic']['intent'],dialogue,c['id'])
        guide=film.render_beatmap(self.plan)
        for s in self.plan['scenes']:
            for field in film.DRAMA_FIELDS[:-1]:
                self.assertIn(s['dramaturgy'][field],guide,(s['number'],field))

    def test_each_beat_plays_once_and_frames_are_states(self):
        for c in self.shots:
            self.assertRegex(c['action'],film.BEATS,c['id'])
            self.assertNotIn(c['cinematic']['blocking'].rstrip('.'),c['action'],c['id'])
            for frame in (c['start_frame'],c['end_frame']):
                self.assertNotIn('Final physical lock',frame,c['id'])
                self.assertNotIn('Framing:',frame,c['id'])
        altered=copy.deepcopy(self.shots)
        shot=altered[0]
        shot['action']=f"Beat 1 (0.0–3.0s): {self.shots[1]['action']} Beat 2 (3.0–6.5s): {shot['cinematic']['blocking']} Beat 3 (6.5–10.0s): He looks on."
        with self.assertRaisesRegex(ValueError,'blocking note replayed'):
            film.validate(self.plan,altered)
        altered=copy.deepcopy(self.shots)
        altered[0]['end_frame']+=' Final physical lock: he steps down.'
        with self.assertRaisesRegex(ValueError,'must be a state'):
            film.validate(self.plan,altered)

    def test_dialogue_fits_one_omni_take(self):
        for c in self.shots:
            spoken=sum(film.syllables(d['text']) for d in c['dialogue'])
            self.assertLessEqual(spoken,film.MAX_CLIP_SYLLABLES,c['id'])
        altered=copy.deepcopy(self.shots)
        altered[0]['dialogue'][0]['text']=' '.join(['nói']*(film.MAX_CLIP_SYLLABLES+1))
        with self.assertRaisesRegex(ValueError,'spoken syllables'):
            film.validate(self.plan,altered)

    def test_prompts_ask_for_one_uncut_natural_take(self):
        for i,c in enumerate(self.shots):
            text=film.render_prompt(self.plan,c,self.shots[i-1] if i else None,
                                    self.shots[i+1] if i<359 else None)
            self.assertIn('In a single continuous shot',text,c['id'])
            for phrase in ('fast-paced','brisk scene pacing','rapid mouth','two rapid','Brisk voice',
                           'briskly and decisively','Final physical lock','[START FRAME','[END FRAME',
                           '[EDIT IN','Next shot ','picture cut','through the seam','at the seam','Edit bridge:'):
                self.assertNotIn(phrase,text,(c['id'],phrase))
            self.assertIn('never flash or cut to an attached character reference portrait',text,c['id'])
            self.assertIn('150-degree' if c['camera']=='H' else '180-degree',text,c['id'])
            self.assertIn(film.CLEAN_FRAME,text,c['id'])
            self.assertIn('TV station or channel logos',text,c['id'])

    def test_each_lead_is_introduced_by_the_narrator_at_first_appearance(self):
        first=film.first_appearances(self.plan,self.shots)
        self.assertEqual(set(first),set(self.plan['identities']))
        for base,cid in first.items():
            intro=[d for d in self.index[cid]['dialogue'] if d['speaker']=='NARRATOR']
            self.assertTrue(intro and self.plan['identities'][base]['name'].casefold() in intro[0]['text'].casefold(),cid)
        narrated={c['id'] for c in self.shots if any(d['speaker']=='NARRATOR' for d in c['dialogue'])}
        self.assertEqual(narrated,set(first.values()))
        self.assertTrue(all(d['speaker']=='NARRATOR' for d in self.index['01.1']['dialogue']))
        altered=copy.deepcopy(self.shots)
        shot=next(c for c in altered if c['id']==first['KIEN'])
        shot['dialogue']=[d for d in shot['dialogue'] if d['speaker']!='NARRATOR']
        with self.assertRaisesRegex(ValueError,'without a narrator introduction'):
            film.validate(self.plan,altered)

    def test_body_mouth_and_face_standard_in_every_prompt(self):
        for i,c in enumerate(self.shots):
            text=film.render_prompt(self.plan,c,self.shots[i-1] if i else None,
                                    self.shots[i+1] if i<359 else None)
            self.assertIn(film.BODY_STANDARD,text,c['id'])
            self.assertIn(film.FACE_STANDARD,text,c['id'])
            mouths=text.split('Mouth map: ',1)[1].split('\n',1)[0]
            for d in c['dialogue']:
                self.assertIn(f"{d['at'][0]:.1f}–{d['at'][1]:.1f}s",mouths,c['id'])
            for d in c['dialogue']:
                if d['mode']=='on':
                    name=self.plan['identities'][film.base_key(self.plan,d['speaker'])]['name'] if d['speaker'] in self.plan['looks'] else ''
                    self.assertIn(f"only {name}" if name else "only ",mouths,c['id'])

    def test_narrator_voice_is_locked_and_calm(self):
        lock=self.plan['narrator']['voice']
        for i,c in enumerate(self.shots):
            text=film.render_prompt(self.plan,c,self.shots[i-1] if i else None,
                                    self.shots[i+1] if i<359 else None)
            narrated=[d for d in c['dialogue'] if d['speaker']=='NARRATOR']
            self.assertEqual(lock in text,bool(narrated),c['id'])
            for d in narrated:
                start,stop=d['at']
                self.assertLessEqual(film.syllables(d['text'])/(stop-start),film.NARRATOR_SYLLABLES_PER_SECOND+1e-9,c['id'])

    def test_each_line_is_timed_inside_the_take_with_its_beat(self):
        for i,c in enumerate(self.shots):
            text=film.render_prompt(self.plan,c,self.shots[i-1] if i else None,
                                    self.shots[i+1] if i<359 else None)
            end=0.0
            for d in c['dialogue']:
                start,stop=d['at']
                self.assertGreaterEqual(start,end,c['id'])
                self.assertLessEqual(film.syllables(d['text'])/(stop-start),film.MAX_SYLLABLES_PER_SECOND+1e-9,c['id'])
                self.assertIn(f"{start:.1f}–{stop:.1f}s · ",text,c['id'])
                end=stop
        altered=copy.deepcopy(self.shots)
        shot=next(c for c in altered if len(c['dialogue'])>1)
        shot['dialogue'][1]['at']=list(shot['dialogue'][0]['at'])
        with self.assertRaisesRegex(ValueError,'overlap or run out of order'):
            film.validate(self.plan,altered)

    def test_no_shot_is_framed_as_television(self):
        altered=copy.deepcopy(self.shots)
        altered[5]['action']=altered[5]['action'].replace('Beat 3','A TV news report plays. Beat 3',1)
        with self.assertRaisesRegex(ValueError,'TV/news wording'):
            film.validate(self.plan,altered)
        altered=copy.deepcopy(self.shots)
        altered[9]['dialogue'][0]['text']='Chuyện này lên truyền hình rồi đó.'
        with self.assertRaisesRegex(ValueError,'TV/news wording'):
            film.validate(self.plan,altered)

    def test_detail_shots_do_not_require_visible_lips(self):
        for c in self.shots:
            if c['camera']=='I':
                self.assertTrue(all(d['mode']!='on' for d in c['dialogue']),c['id'])

    def test_watch_does_not_break_before_its_impact_or_open_twice(self):
        before=film.prop_detail(self.plan,'WATCH',self.index['08.1'])
        impact=film.prop_detail(self.plan,'WATCH',self.index['08.4'])
        after=film.prop_detail(self.plan,'WATCH',self.index['08.6'])
        self.assertIn('intact and running',before)
        self.assertIn('impact dents the closed case and stops it',impact)
        self.assertIn('has stopped',after)
        self.assertIn('lid CLOSED',before)
        self.assertIn('Do not open',film.prop_detail(self.plan,'WATCH',self.index['06.5']))

    def test_runner_attaches_only_visible_and_picture_references(self):
        # Compile just these pure helpers: importing the full runner would load
        # CMS/network integration and create runtime directories unnecessarily.
        path=film.BASE_DIR.parent/'flowkit/runners/ke_song_sot.py'
        parsed=ast.parse(path.read_text())
        helpers=[n for n in parsed.body if isinstance(n,ast.FunctionDef) and
                 n.name in ('get_clip_reference_media_ids','is_new_scene_clip')]
        specs=[{'tag':x['tag'],'aliases':[x['tag'],x['name']]} for x in self.plan['identities'].values()]
        mids={x['tag']:x['media_id'] for x in self.plan['identities'].values()}
        scope={'CHARACTER_SPECS':specs,'LOCKED_CHARACTER_MEDIA_IDS':mids}
        exec(compile(ast.Module(body=helpers,type_ignores=[]),str(path),'exec'),scope)
        for i,c in enumerate(self.shots):
            text=film.render_prompt(self.plan,c,self.shots[i-1] if i else None,
                                    self.shots[i+1] if i<359 else None)
            bases={film.base_key(self.plan,k) for k in c['characters']}|set(c.get('image_references',[]))
            expected={self.plan['identities'][k]['media_id'] for k in bases}
            self.assertEqual(set(scope['get_clip_reference_media_ids'](text)),expected,c['id'])
            new=scope['is_new_scene_clip'](text,c['number'],'a-valid-start-frame')
            self.assertEqual(new,c['transition']!='CONTINUE',c['id'])
        self.assertEqual(scope['get_clip_reference_media_ids']('[CHARACTERS — approved identities and current appearances]\nNo lead visible.\n[EDIT IN]\n@Son was in the previous shot.'),[])


if __name__=='__main__':
    unittest.main()
