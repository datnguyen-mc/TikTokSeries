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
