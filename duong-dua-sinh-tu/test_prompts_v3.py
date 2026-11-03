"""Regression checks for the 40-minute (240-shot) film's editorial and story continuity contracts."""
import ast
import copy
import json
import unittest

import build_prompts_v3 as film


class FilmContinuityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = json.loads((film.BASE_DIR / 'PHAN_CANH_V3.json').read_text(encoding='utf-8'))
        cls.shots = film.normalize(cls.plan)
        cls.index = {c['id']: c for c in cls.shots}

    def test_whole_film_is_valid(self):
        film.validate(self.plan, self.shots)
        self.assertEqual(len(self.shots), 240)
        self.assertEqual(len(list(zip(self.shots, self.shots[1:]))), 239)

    def test_continuation_uses_exact_end_without_repeating_action(self):
        for a, b in zip(self.shots, self.shots[1:]):
            if b['transition'] == 'CONTINUE':
                self.assertEqual(b['start_frame'], a['end_frame'], b['id'])
                self.assertEqual(
                    (b['location'], b['camera'], b['story_time']),
                    (a['location'], a['camera'], a['story_time']),
                    b['id'],
                )
                self.assertNotEqual(b['action'], a['action'], b['id'])

    def test_location_change_cannot_masquerade_as_continuation(self):
        altered = copy.deepcopy(self.shots)
        shot = altered[1]
        shot['transition'] = 'CONTINUE'
        shot['location'] = 'TOTO_DINER' if shot['location'] != 'TOTO_DINER' else 'HIGHWAY_NIGHT'
        with self.assertRaisesRegex(ValueError, 'changes location/camera/time'):
            film.validate(self.plan, altered)

    def test_replayed_action_and_injected_spoken_tags_are_rejected(self):
        altered = copy.deepcopy(self.shots)
        altered[1]['action'] = altered[0]['action']
        with self.assertRaisesRegex(ValueError, 'action repeats'):
            film.validate(self.plan, altered)
        altered = copy.deepcopy(self.shots)
        next(c for c in altered if c['dialogue'])['dialogue'][0]['text'] += ' @Tom'
        with self.assertRaisesRegex(ValueError, 'injected tag/quote'):
            film.validate(self.plan, altered)

    def test_generator_mode_matches_actual_edit_type(self):
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertTrue(text.startswith('[FORMAT]'), c['id'])
            self.assertNotIn('2.39:1', text)
            self.assertNotIn('0.5s', text)
            self.assertNotIn('one slow-motion beat', text)
            self.assertNotIn('[project LIST]', text)

    def test_all_handoffs_are_exported_and_output_is_deterministic(self):
        out = film.outputs(self.plan, self.shots)
        self.assertEqual(out, film.outputs(self.plan, film.normalize(self.plan)))
        self.assertEqual(len([p for p in out if '/clip-' in p]), 240)
        table = out['BANG_NOI_CLIP.md']
        for a, b in zip(self.shots, self.shots[1:]):
            self.assertIn(f"[{a['id']}]({film.ref(a)}) → [{b['id']}]({film.ref(b)})", table)
        self.assertEqual(len(out), 326 if film.edition(self.plan) == '3.1' else 325)
        manifest = json.loads(out['RENDER_MANIFEST_V3.json'])
        self.assertEqual(len(manifest['clips']), 240)

    def test_detailed_edition_cannot_silently_omit_directing(self):
        incomplete = copy.deepcopy(self.plan)
        incomplete['editorial_revision'] = '3.1'
        incomplete['scenes'][0]['clips'][0].pop('cinematic', None)
        with self.assertRaisesRegex(ValueError, 'incomplete specific directing detail'):
            film.validate(incomplete, film.normalize(incomplete))

    def test_scene_and_shot_details_are_exported_without_new_dialogue(self):
        for i, c in enumerate(self.shots):
            prompt = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            for field in film.DETAIL_FIELDS:
                self.assertIn(c['cinematic'][field], prompt, (c['id'], field))
            dialogue = prompt.split('[DIALOGUE]\n', 1)[1].split('\n[PROPS]', 1)[0]
            self.assertNotIn(c['cinematic']['intent'], dialogue, c['id'])
        guide = film.render_beatmap(self.plan)
        for s in self.plan['scenes']:
            for field in film.DRAMA_FIELDS[:-1]:
                self.assertIn(s['dramaturgy'][field], guide, (s['number'], field))

    def test_each_beat_plays_once_and_frames_are_states(self):
        for c in self.shots:
            self.assertRegex(c['action'], film.BEATS, c['id'])
            self.assertNotIn(c['cinematic']['blocking'].rstrip('.'), c['action'], c['id'])
            for frame in (c['start_frame'], c['end_frame']):
                self.assertNotIn('Final physical lock', frame, c['id'])
                self.assertNotIn('Framing:', frame, c['id'])

    def test_dialogue_fits_one_omni_take(self):
        for c in self.shots:
            spoken = sum(film.syllables(d['text']) for d in c['dialogue'])
            self.assertLessEqual(spoken, film.MAX_CLIP_SYLLABLES, c['id'])

    def test_prompts_ask_for_one_uncut_natural_take(self):
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertIn('[GLOBAL VOICE SPEED RULE — 1.25x]', text, c['id'])
            self.assertIn('1.25x normal conversational speaking speed (125%)', text, c['id'])
            self.assertIn('In a single continuous shot', text, c['id'])
            self.assertIn('never flash or cut to an attached character reference portrait', text, c['id'])
            self.assertIn('150-degree' if c['camera'] == 'H' else '180-degree', text, c['id'])
            self.assertIn(film.CLEAN_FRAME, text, c['id'])
            self.assertIn('TV station or channel logos', text, c['id'])

    def test_each_lead_is_introduced_by_the_narrator_at_first_appearance(self):
        first = film.first_appearances(self.plan, self.shots)
        self.assertEqual(set(first), set(self.plan['identities']))
        for base, cid in first.items():
            intro = [d for d in self.index[cid]['dialogue'] if d['speaker'] == 'NARRATOR']
            self.assertTrue(intro and self.plan['identities'][base]['name'].casefold() in intro[0]['text'].casefold(), cid)
        narrated = {c['id'] for c in self.shots if any(d['speaker'] == 'NARRATOR' for d in c['dialogue'])}
        self.assertEqual(narrated, set(first.values()))

    def test_body_mouth_and_face_standard_in_every_prompt(self):
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertIn(film.BODY_STANDARD, text, c['id'])
            self.assertIn(film.FACE_STANDARD, text, c['id'])
            mouths = text.split('Mouth map: ', 1)[1].split('\n', 1)[0]
            for d in c['dialogue']:
                self.assertIn(f"{d['at'][0]:.1f}–{d['at'][1]:.1f}s", mouths, c['id'])

    def test_narrator_voice_is_locked_and_calm(self):
        lock = self.plan['narrator']['voice']
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            narrated = [d for d in c['dialogue'] if d['speaker'] == 'NARRATOR']
            self.assertEqual(lock in text, bool(narrated), c['id'])
            for d in narrated:
                start, stop = d['at']
                self.assertLessEqual(
                    film.syllables(d['text']) / (stop - start), film.NARRATOR_SYLLABLES_PER_SECOND + 1e-9, c['id']
                )

    def test_each_line_is_timed_inside_the_take_with_its_beat(self):
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            end = 0.0
            for d in c['dialogue']:
                start, stop = d['at']
                self.assertGreaterEqual(start, end, c['id'])
                self.assertLessEqual(
                    film.syllables(d['text']) / (stop - start), film.MAX_SYLLABLES_PER_SECOND + 1e-9, c['id']
                )
                self.assertIn(f"{start:.1f}–{stop:.1f}s · ", text, c['id'])
                end = stop

    def test_no_shot_is_framed_as_television(self):
        altered = copy.deepcopy(self.shots)
        altered[5]['action'] = altered[5]['action'].replace('Beat 3', 'A TV news report plays. Beat 3', 1)
        with self.assertRaisesRegex(ValueError, 'TV/news wording'):
            film.validate(self.plan, altered)

    def test_detail_shots_do_not_require_visible_lips(self):
        for c in self.shots:
            if c['camera'] == 'I':
                self.assertTrue(all(d['mode'] != 'on' for d in c['dialogue']), c['id'])

    def test_runner_attaches_only_visible_and_picture_references(self):
        path = film.BASE_DIR.parent / 'flowkit/runners/duong_dua_sinh_tu.py'
        parsed = ast.parse(path.read_text(encoding='utf-8'))
        helpers = [
            n for n in parsed.body
            if isinstance(n, ast.FunctionDef) and n.name in ('get_clip_reference_media_ids', 'is_new_scene_clip')
        ]
        specs = [{'tag': x['tag'], 'aliases': [x['tag'], x['name']]} for x in self.plan['identities'].values()]
        mids = {x['tag']: x['media_id'] for x in self.plan['identities'].values()}
        scope = {'CHARACTER_SPECS': specs, 'LOCKED_CHARACTER_MEDIA_IDS': mids}
        exec(compile(ast.Module(body=helpers, type_ignores=[]), str(path), 'exec'), scope)
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            bases = {film.base_key(self.plan, k) for k in c['characters']} | set(c.get('image_references', []))
            expected = {self.plan['identities'][k]['media_id'] for k in bases}
            self.assertEqual(set(scope['get_clip_reference_media_ids'](text)), expected, c['id'])
            new = scope['is_new_scene_clip'](text, c['number'], 'a-valid-start-frame')
            self.assertTrue(new, c['id'])
        self.assertEqual(
            scope['get_clip_reference_media_ids'](
                '[CHARACTERS — approved identities and current appearances]\nNo lead visible.\n[EDIT IN]\n@Tom was in the previous shot.'
            ),
            [],
        )

    def test_global_film_bible_completeness(self):
        from film_bible import GLOBAL_FILM_BIBLE
        self.assertEqual(len(GLOBAL_FILM_BIBLE['CHARACTER_LOCK']), 12)
        self.assertEqual(len(GLOBAL_FILM_BIBLE['VEHICLE_LOCK']), 11)
        self.assertEqual(len(GLOBAL_FILM_BIBLE['ENVIRONMENT_LOCK']), 20)
        self.assertEqual(len(GLOBAL_FILM_BIBLE['OBJECT_LOCK']), 11)
        for v in GLOBAL_FILM_BIBLE['VEHICLE_LOCK'].values():
            self.assertIn('wheels', v['wheels_axles'].lower())
            self.assertIn(v['steering_side'], ('LEFT', 'CENTER'))
            self.assertTrue(v['damage_states'])
        for env in GLOBAL_FILM_BIBLE['ENVIRONMENT_LOCK'].values():
            self.assertTrue(env.get('orientation_axis'))

    def test_no_duplicate_character_references_or_self_eyelines(self):
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertIsNone(film.DUPLICATE_CHAR_PAIR.search(text), c['id'])
        altered = copy.deepcopy(self.shots)
        altered[0]['cinematic']['composition'] = 'Frame Verni and Verni with the rig 18 in the E lens.'
        with self.assertRaisesRegex(ValueError, 'duplicate character reference'):
            film.validate(self.plan, altered)

    def test_drivers_are_inside_vehicles_during_highway_and_cockpit_scenes(self):
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertIsNone(film.DRIVER_OUTSIDE_MOVING_VEHICLE.search(text), c['id'])
            if c['location'] in ('HIGHWAY_NIGHT', 'RIG_CABIN', 'RACE_COCKPIT', 'LA_HILLS_ROAD', 'RAIL_CROSSING'):
                self.assertIsNone(film.STOPPING_CAMERA_IN_PURSUIT.search(text), c['id'])
        altered = copy.deepcopy(self.shots)
        altered[0]['start_frame'] = (
            'In HIGHWAY_NIGHT during N1 night: Verni positioned in the primary foreground plane beside the rig 18 at 110 km/h.'
        )
        with self.assertRaisesRegex(ValueError, 'driver described as outside/beside a moving highway/cockpit vehicle'):
            film.validate(self.plan, altered)

    def test_insert_shots_have_no_forced_visible_characters_and_use_offscreen_speech(self):
        insert_shots = [c for c in self.shots if c['camera'] == 'I']
        self.assertGreaterEqual(len(insert_shots), 10)
        for c in insert_shots:
            self.assertEqual(c['characters'], [], c['id'])
            self.assertEqual(c.get('shot_type'), 'INSERT_DETAIL', c['id'])
            self.assertTrue(all(d['mode'] != 'on' for d in c['dialogue']), c['id'])
            refs = film.select_shot_references(self.plan, c)
            self.assertEqual(refs, [], c['id'])

    def test_persistent_vehicle_and_object_state_tracking(self):
        s05 = self.index['05.1']['entity_state']['vehicles']['ECLIPSE']
        s15 = self.index['15.2']['entity_state']['vehicles']['ECLIPSE']
        s19 = self.index['19.2']['entity_state']['vehicles']['ECLIPSE']
        self.assertIn('pristine', s05)
        self.assertIn('floor panel', s15)
        self.assertIn('theatrical orange smoke', s19)
        s24 = self.index['24.1']['entity_state']['vehicles']['CHARGER']
        s40 = self.index['40.1']['entity_state']['vehicles']['CHARGER']
        self.assertIn('pristine', s24)
        self.assertIn('dented', s40)

    def test_action_stunt_choreography_and_no_blood_gore_rule(self):
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertIn('Clean athletic precision, all movements are simulated stunt choreography.', text, c['id'])
            self.assertIn('fast defensive movements, precise dodges, controlled footwork', text.casefold(), c['id'])
            self.assertIn("outside the camera's view", text, c['id'])
            for field in ('start_frame', 'action', 'end_frame', 'lighting', 'wardrobe_note'):
                self.assertIsNone(film.UNSAFE_VIOLENCE_OR_GORE_WORDS.search(c.get(field, '')), f"{c['id']} {field}")
            for d in c['dialogue']:
                self.assertIsNone(film.UNSAFE_VIOLENCE_OR_GORE_WORDS.search(d['text']), f"{c['id']} dialogue")
        s08_1 = film.render_prompt(self.plan, self.index['08.1'], self.index['07.6'], self.index['08.2'])
        self.assertIn('Two professional stunt performers', s08_1)
        self.assertIn("lands safely onto padded flooring outside the camera's view", s08_1)

        unsafe = copy.deepcopy(self.shots)
        unsafe[0]['action'] = unsafe[0]['action'].replace('Beat 1', 'Beat 1 (throw a punch with a bloody wound)')
        with self.assertRaisesRegex(ValueError, 'unsafe violence/gore/injury wording'):
            film.validate(self.plan, unsafe)

    def test_no_adjacent_lead_names_double_articles_or_boilerplate_intent(self):
        for i, c in enumerate(self.shots):
            self.assertNotEqual(c['transition'], 'CONTINUE', c['id'])
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertIsNone(film.ADJACENT_LEAD_NAMES.search(text), c['id'])
            self.assertIsNone(film.DOUBLE_ARTICLE_OR_RAW_LENS.search(text), c['id'])
            self.assertIsNone(film.BOILERPLATE_INTENT.search(text), c['id'])

    def test_spatial_state_and_180_degree_axis_preserved(self):
        for i, c in enumerate(self.shots):
            sp = c.get('spatial_state') or {}
            self.assertTrue(sp.get('axis'), c['id'])
            self.assertTrue(sp.get('shot_type'), c['id'])
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertIn('Spatial geography & 180-degree axis:', text, c['id'])

    def test_omni_model_capability_validation_and_auto_repair(self):
        broken = copy.deepcopy(self.shots[0])
        broken['cinematic']['composition'] = 'Frame Verni and Verni with the rig 18.'
        broken['start_frame'] = 'In HIGHWAY_NIGHT: Verni positioned in the primary foreground plane beside the rig 18.'
        repaired = film.auto_repair_shot(self.plan, broken, None)
        self.assertIsNone(film.DUPLICATE_CHAR_PAIR.search(repaired['cinematic']['composition']))
        self.assertIsNone(film.DRIVER_OUTSIDE_MOVING_VEHICLE.search(repaired['start_frame']))
        for c in self.shots:
            refs = film.select_shot_references(self.plan, c)
            self.assertLessEqual(len(refs), 7, c['id'])
            wf = film.determine_omni_workflow(self.plan, c)
            self.assertIn(wf, ('ingredients', 'frames', 'insert', 'text'), c['id'])

    def test_moving_vehicles_enforce_spinning_wheels_same_direction_and_priority_sfx(self):
        moving_clips = [c for c in self.shots if (c.get('spatial_state') or {}).get('moving_vehicle_clip')]
        self.assertGreaterEqual(len(moving_clips), 90)
        for i, c in enumerate(self.shots):
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertIn('SOUND EFFECTS PRIORITY:', text, c['id'])
            self.assertIn('stationary or frozen wheels on moving vehicles', text, c['id'])
            if (c.get('spatial_state') or {}).get('moving_vehicle_clip'):
                self.assertIn('Vehicle motion & wheel lock:', text, c['id'])
                self.assertIn('wheels spinning rapidly forward with realistic rotational motion blur', text, c['id'])
                self.assertIn('co-directional forward direction (left-to-right along the road axis)', text, c['id'])
                self.assertIn('HIGH-PRIORITY AUTOMOTIVE SFX:', text, c['id'])

    def test_action_gesture_dialogue_and_cast_precision(self):
        import re
        identities = self.plan['identities']
        looks = self.plan['looks']
        all_lead_names = {identities[k]['name']: k for k in identities}
        veh_poss_re = re.compile(
            r"\b(?:Tom|Micdo|Verni|Ny Tran|Seja|Cina|Cela|Cevin|Onle)'s\s+"
            r"(?:deep-red|red|neon-green|smoking|metallic-orange|orange|matte-black|black|jet-black|white|alpine-white|"
            r"18-wheel|18-wheeler|massive|silver|swerving|trailing|stopped|lead|idling|second|third|#2|#3|men|crew|departure|car|coupe|truck|pickup|motorcycle|bike|"
            r"RX7|RX-7|ECLIPSE|Eclipse|SUPRA|Supra|F150_TRUCK|RIG_18|CHARGER|Charger|JETTA|Jetta|S2000)\b",
            re.IGNORECASE,
        )
        for c in self.shots:
            cid = c['id']
            d = [x for x in c['dialogue'] if x['speaker'] != 'NARRATOR'][0]
            t1, t2 = d['at']
            spk_name = identities[looks[d['speaker']][0]]['name']
            m_b2 = re.search(r"Beat 2 \((\d+\.\d)–(\d+\.\d)s\): (.*?)\. Beat 3", c['action'])
            self.assertIsNotNone(m_b2, f"{cid}: missing Beat 2 window")
            bt1, bt2, b2_txt = float(m_b2.group(1)), float(m_b2.group(2)), m_b2.group(3)
            self.assertAlmostEqual(bt1, t1, places=1, msg=f"{cid}: Beat 2 start != dialogue start")
            self.assertAlmostEqual(bt2, t2, places=1, msg=f"{cid}: Beat 2 end != dialogue end")
            if c.get('shot_type') == 'INSERT_DETAIL':
                self.assertIn(f"While {spk_name}'s voice plays off screen", b2_txt, cid)
            else:
                self.assertTrue(b2_txt.startswith(spk_name), f"{cid}: Beat 2 does not start with speaker {spk_name}: {b2_txt}")
                assigned_names = [identities[looks[k][0]]['name'] for k in c['characters']]
                clean_txt = veh_poss_re.sub('the vehicle', f"{c['start_frame']} {c['action']} {c['end_frame']}")
                present_names = [nm for nm in all_lead_names if re.search(rf"\b{re.escape(nm)}\b", clean_txt)]
                self.assertEqual(set(assigned_names), set(present_names), f"{cid}: cast {assigned_names} != present {present_names}")

    def test_camera_angle_and_surrounding_objects_precision(self):
        from film_bible import ENVIRONMENT_LOCK
        for loc_id, env in ENVIRONMENT_LOCK.items():
            self.assertNotIn('none (open', env.get('interior_furniture_objects', '').lower(), loc_id)
            self.assertTrue(env.get('surface_textures'), loc_id)
            self.assertTrue(env.get('architecture_layout'), loc_id)
            self.assertTrue(env.get('terrain_landmarks'), loc_id)

        for i, c in enumerate(self.shots):
            cid = c['id']
            loc_id = c['location']
            env = ENVIRONMENT_LOCK[loc_id]
            text = film.render_prompt(
                self.plan, c, self.shots[i - 1] if i else None, self.shots[i + 1] if i < 239 else None
            )
            self.assertIn('Architecture & road geometry:', text, cid)
            self.assertIn('Surrounding objects & landmarks:', text, cid)
            self.assertIn(f"Surrounding environment objects in {loc_id}:", text, cid)
            self.assertEqual(c['cinematic']['texture'], env['surface_textures'], cid)
            comp = c['cinematic']['composition']
            self.assertTrue(
                any(
                    rig in comp
                    for rig in (
                        'interior cabin-mounted camera angle',
                        'low-angle exterior pursuit tracking camera rig',
                        'eye-level cinematic camera setup',
                        'Macro detail insert composition',
                        '85mm',
                    )
                ),
                f"{cid}: missing explicit camera rig/angle in composition: {comp}",
            )
            self.assertIn(env['interior_furniture_objects'], comp, cid)
            self.assertIn(env['terrain_landmarks'], c['cinematic']['focus'], cid)
            if loc_id == 'TOTO_BACKYARD':
                self.assertNotIn('WRENCH_KIT', c['props'], cid)


if __name__ == '__main__':
    unittest.main()
