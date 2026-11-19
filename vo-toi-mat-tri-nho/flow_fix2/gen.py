#!/usr/bin/env python3
"""Câu lệnh Flow bản sửa 2 (19/11): cảnh thoại luôn giữ người đang nói trong khung; cận đồ vật chỉ ở chỗ không thoại.
Sinh fix2.json = {id: [nhân vật[], câu lệnh]} để dán vào Flow."""
import json, re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def chars_from(path):
    out = {}
    for ln in open(os.path.join(ROOT, path)):
        m = re.match(r'- @\w+ = (.*Attached image: "(.+?)"\.)', ln.strip())
        if m: out[m.group(2)] = "- " + m.group(1)
    return out
C = {}
for p in ["flow_15s_fix/08-1.txt", "flow_15s_fix/14-2.txt", "flow_15s_fix/22-1.txt", "flow_15s/p09/09-1.txt"]: C.update(chars_from(p))
VOICE = {
 "Quân": "man of 36, smooth warm baritone, confident and charming, a little boyish",
 "Linh": "woman of 32, warm low alto with a soft husky edge, elegant and unhurried, never raises her voice, crisp Hà Nội diction",
 "Tuấn": "man of 35, light bright tenor, slightly nasal and quick, eager to please, words tumbling out",
 "Mai Anh": "young woman of 25, bright sweet soprano with a playful lilt, light and quick",
}
STYLE = ("Photorealistic live-action Vietnamese romantic comedy-drama with a thriller edge, in the style of a premium anamorphic feature film, 24 fps; "
         "rich teal-and-amber grade, motivated practical light, natural skin texture with pores, subtle 35mm film grain, shallow depth of field with creamy oval bokeh, "
         "gentle halation. Real actors, believable understated performances, a premium theatrical feature — never CGI, never an advertisement.")
AVOID = ("Camera brand logos, camera data or recording overlays, character names or @handles written on screen, sparkle or star watermarks, rounded frame borders, black bars, "
         "visible film cameras, tripods, light stands, boom microphones, film crew or any filmmaking equipment anywhere in the frame, phone camera interfaces, "
         "the same character appearing twice in one shot, on-screen text of any kind (subtitles, captions, titles, watermarks, logos), readable writing, blurry faces, distorted hands, "
         "background music, letterbox bars, cuts at any other moment, extra people in focus, face, hair or costume changes, props on the table changing between shots, "
         "a line spoken while the speaker is off screen, a cutaway or insert shot during dialogue, robotic or text-to-speech sounding voices, flat monotone delivery, slurred speech, "
         "repeated, stuttered or echoed words, the line spoken twice, an off-screen narrator or voice-over, Southern or Central Vietnamese accents, flashes of white, fades to white.")
def build(chars, loc, shots, beats, turns, sfx, props=None):
    cuts = [s[1] for s in shots[:-1]]
    n = len(shots)
    t = [f"A 15-second live-action film sequence of {n} shot{'s' if n > 1 else ''}, 16:9 widescreen, 24 fps, "
         + (f"with hard cuts only at {', '.join(f'{c:g}s' for c in cuts)}" if cuts else "one continuous take with no cuts")
         + "; one place and one moment, sound and action continuous across the cuts.", "", "[STYLE]", STYLE, "", "[LOCATION]", loc]
    if props: t += ["", "[PROPS — identical in every shot]", props]
    t += ["", "[CHARACTERS]", "Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, and never flash the studio reference portrait; the characters are already in place in the very first frame."]
    t += [C[c] for c in chars] + ["Nobody else appears in focus.", "", "[SHOT LIST — hard cuts only at the marked seconds]"]
    for i, (a, b, d) in enumerate(shots, 1): t.append(f"- Shot {i}, {a:g}–{b:g}s: {d}")
    t += ["- Rule for every line of dialogue: the person speaking stays on screen, face and moving lips clearly visible, for the whole line; never cut away or show an object while anyone is talking.", "",
          "[TIMELINE — second by second]", "Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per beat."]
    for i, (a, b, d) in enumerate(beats): t.append(f"- {a:g}–{b:g}s ({'Shot ' + str(i + 1) if i == 0 else 'CUT to Shot ' + str(i + 1)}): {d}" if len(beats) == len(shots) else f"- {a:g}–{b:g}s: {d}")
    t[-1] += " The sequence settles on this as its final frame."
    t += ["", "[AUDIO]"]
    if turns:
        t.append(f"- Dialogue in Vietnamese with exact lip-sync, {len(turns)} spoken turn{'s' if len(turns) > 1 else ''} in this order, each said exactly once (no subtitles):")
        for k, (a, b, who, how, line) in enumerate(turns, 1):
            t.append(f"- Turn {k}, {a:g}–{b:g}s, spoken on screen by {who} ({VOICE[who]}, {how}): \"{line}\"")
        t += ["- Throughout, only the person whose turn it is moves the lips while anyone else listens with the mouth closed; real breaths and tiny natural hesitations, close, natural dialogue sound with a little room tone — it sounds like real actors talking, never like a voice-over or text-to-speech.",
              "- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and different characters sound clearly different in pitch, age and texture.",
              f"- All speech is over by {turns[-1][1]:g}s; outside the turns above nobody says a word, and no line is ever repeated to fill the time.",
              "- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud."]
    else:
        t.append("- No dialogue at all: nobody speaks a single word.")
    t += [f"- SFX: {sfx} No music.", "", "[AVOID]", AVOID]
    return [chars, "\n".join(t)]
LAKE = "A cosy lakeside street-food corner at night: low blue plastic stools, one small square steel table by the water, a smoky charcoal grill behind, strings of warm yellow bulbs overhead, reflections on the dark lake; warm smoky gold light."
TABLE = ("On the small steel table, the same items in every shot and nothing else: one plate of grilled pork skewers, two small bowls of rice noodles with fresh herbs, "
         "one tall glass of iced black coffee, two plain glasses of iced green tea, a cup of chopsticks. Nobody brings new food or drinks.")
QH, LH = "Quân · Hẹn hò", "Linh · Hẹn hò"
SFX_LAKE = "charcoal sizzling, motorbikes passing slowly far away, water lapping, soft distant chatter."
P = {}
P["09-1"] = build([QH, LH], LAKE, [(0, 3, "35mm wide shot of the lakeside food corner and the couple at the small table, a slow crane-down."),
                                    (3, 9, "50mm two-shot across the small steel table, the husband on the left and the wife on the right, both faces clearly visible in profile-three-quarter, a completely static frame."),
                                    (9, 15, "85mm close-up on the husband over the wife's shoulder, eyes in sharp focus, background melting into bokeh, a completely static frame.")],
    [(0, 3, "Smoke and yellow bulbs over the lake; Quan pulls out a low blue stool for Linh and she sits down at the small table. No one speaks."),
     (3, 9, "Quan proudly slides the tall glass of iced black coffee across to Linh and speaks; then Linh glances at the glass, not at him, and answers flatly."),
     (9, 15, "Quan, baffled, holds up two fingers and speaks.")],
    [(3.3, 6.8, "Quân", "speaking at a natural conversational pace, proud", "Quán đầu tiên anh đưa em đi. Cà phê đen không đường, đúng không?"),
     (7.1, 8.6, "Linh", "speaking slowly and softly, flat", "Tôi ghét cà phê đen."),
     (9.4, 12.2, "Quân", "speaking quickly in short lively phrases, every word clear, baffled", "Ghét? Mười năm nay sáng nào em cũng pha hai cốc!")], SFX_LAKE, TABLE)
P["09-2"] = build([LH, QH], LAKE, [(0, 6, "85mm close-up on the wife, eyes in sharp focus, background melting into bokeh, a slow lateral dolly."),
                                    (6, 11, "85mm close-up on the husband, eyes in sharp focus, background melting into bokeh, a slow, steady push-in."),
                                    (11, 15, "50mm two-shot across the small steel table, both faces visible, a completely static frame.")],
    [(0, 6, "Linh watches the bulbs reflected in the dark lake and speaks, far away."),
     (6, 11, "The slowest push-in on Quan's stunned face; he speaks quietly."),
     (11, 15, "Linh gently slides the iced black coffee back to Quan's side and picks up her own glass of iced green tea, a small smile. No one speaks.")],
    [(0.4, 4.6, "Linh", "speaking slowly and softly with small natural pauses, far away", "Vì có người thích cà phê đen. Nên cô ấy uống cùng cho có đôi."),
     (6.3, 9.0, "Quân", "speaking slowly and softly with small natural pauses, quiet", "Mười năm… anh chưa từng hỏi em thích gì.")], SFX_LAKE, TABLE)
P["09-3"] = build([QH, LH], LAKE, [(0, 6.5, "50mm two-shot across the small steel table, both faces clearly visible, a slow, steady push-in."),
                                    (6.5, 15, "85mm close-up on the wife over the husband's shoulder, eyes in sharp focus, background melting into bokeh, a completely static frame.")],
    [(0, 6.5, "Quan leans forward over the table, hopeful, hands together, and asks."),
     (6.5, 15, "Linh holds up five fingers, then folds them away one by one as she answers, lips curling into a teasing smile; she sips her iced green tea.")],
    [(0.4, 4.6, "Quân", "speaking at a natural conversational pace, hopeful", "Thế buổi hẹn hôm nay được mấy điểm? Có hẹn lần hai không?"),
     (6.9, 11.4, "Linh", "speaking slowly and softly with small natural pauses, teasing", "Năm điểm. Trừ năm điểm vì đến muộn mười năm.")], SFX_LAKE, TABLE)
P["09-4"] = build([QH, LH], "A quiet lakeside promenade at night beside the same street-food corner: a low stone edge, old trees, strings of warm yellow bulbs, their reflections trembling on the dark lake; warm gold and deep teal light.",
    [(0, 5, "35mm wide shot from behind, a slow tracking dolly following the couple."),
     (5, 10, "50mm two-shot walking side by side, a slow backward tracking shot in front of them."),
     (10, 15, "24mm wide shot of the lakeside, a slow crane-up as the couple walks away into the lights.")],
    [(0, 5, "After dinner Quan and Linh walk slowly along the lake edge, a small gap between them. No one speaks."),
     (5, 10, "Quan steals a glance at Linh; she pretends not to notice but the corner of her mouth lifts. No one speaks."),
     (10, 15, "They keep walking, the gap between them a little smaller, bulbs reflected in the water. No one speaks.")],
    [], "footsteps on stone, water lapping, a light night breeze, faraway motorbikes.")
P["14-2"] = build(["Quân · Vest navy", "Tuấn · Vest be"], "A glass-walled CEO office high above the city: long walnut desk, white leather sofa, shelves of fabric and wood samples, panoramic skyline; cool white-blue light.",
    [(0, 6, "50mm medium shot of the assistant standing beside the desk, a subtle restless handheld float."),
     (6, 10.5, "50mm medium shot of the husband seated at the desk, a completely static frame."),
     (10.5, 15, "35mm two-shot of both men at the desk, a slow, steady push-in.")],
    [(0, 6, "Tuan juggles a blue envelope and a pink envelope from hand to hand, squinting at them, and mutters."),
     (6, 10.5, "Quan, busy writing at the desk, does not look up; he only waves a hand. No one speaks."),
     (10.5, 15, "Tuan swaps the envelopes behind his back and sets them down on the desk with a confident nod; Quan looks up slowly, with dawning dread. No one speaks.")],
    [(0.5, 4.5, "Tuấn", "speaking quickly in short lively phrases, every word clear, muttering", "Xanh cho chị Linh, hồng cho Mai Anh… hay ngược lại nhỉ?")],
    "a quiet office hum, the city far below, paper rustling.")
P["22-1"] = build(["Quân · Linen kem", "Linh · Voan trắng"], "A villa garden at night dressed for a party: strings of warm fairy lights, a white rose arch, a small table with a birthday cake and candles, lanterns, a pool reflecting the lights.",
    [(0, 3, "35mm wide shot of the garden party with the couple under the white rose arch, a slow crane-down."),
     (3, 9, "50mm side two-shot: the husband on one knee and the wife standing before him, both faces clearly visible, a slow, steady push-in."),
     (9, 15, "85mm close-up on the wife, eyes in sharp focus, background melting into bokeh, a completely static frame.")],
    [(0, 3, "Fairy lights glow over the garden; Quan sinks onto one knee beneath the white rose arch in front of Linh. No one speaks."),
     (3, 9, "Quan opens a small red velvet ring box and holds it up to Linh, nervous and sincere, and speaks."),
     (9, 15, "Linh, in white chiffon, plays it cool, fighting a smile, and answers.")],
    [(3.4, 7.4, "Quân", "speaking at a natural conversational pace, nervous, sincere", "Cô gái hai mươi hai tuổi ơi, em có đồng ý lấy anh không?"),
     (9.4, 12.2, "Linh", "speaking slowly and softly with small natural pauses, playing along", "Nhanh thế? Tôi còn chưa biết gì về anh.")],
    "crickets, a soft breeze in the fairy lights, distant laughter, the pool lapping.")
P["23-1"] = build(["Linh · Voan trắng", "Quân · Linen kem"], "A villa garden at night dressed for a party: strings of warm fairy lights, a white rose arch, a small table with a birthday cake and candles, lanterns, a pool reflecting the lights.",
    [(0, 9, "50mm two-shot of the wife and the husband standing by the small cake table, both faces clearly visible, a slow, steady push-in."),
     (9, 15, "85mm close-up on the husband, eyes in sharp focus, background melting into bokeh, a subtle restless handheld float.")],
    [(0, 9, "Linh holds up a white sheet of paper beside her face, businesslike, eyes sparkling, and speaks; then she taps the paper and speaks again; the paper is held edge-on, never readable."),
     (9, 15, "Quan grabs the pen from the table, eager, and answers.")],
    [(0.4, 3.6, "Linh", "speaking at a natural conversational pace, businesslike", "Hợp đồng thử việc làm chồng. Sáu tháng."),
     (4.6, 7.8, "Linh", "speaking at a natural conversational pace, crisp", "Điều một: sáng nào cũng đưa con đi học."),
     (9.6, 11.2, "Quân", "speaking quickly in short lively phrases, every word clear, eager", "Đồng ý! Điều hai?")],
    "crickets, a soft breeze in the fairy lights, distant laughter, the pool lapping.")
P["08-1"] = build(["Linh · Cô gái 22", "Mai Anh · Đồ yoga"], "A glass sunroom full of plants inside the villa, two yoga mats on a wooden floor; sunlight dappled through leaves.",
    [(0, 3, "35mm wide shot of the glass sunroom with both women on their mats, a slow lateral dolly."),
     (3, 8, "50mm two-shot of both women sitting on the yoga mats, both faces clearly visible, a completely static frame."),
     (8, 15, "85mm close-up on the wife, eyes in sharp focus, background melting into bokeh, a slow, steady push-in.")],
    [(0, 3, "Sunlight through leaves; Linh and Mai Anh sit cross-legged on their yoga mats. No one speaks."),
     (3, 8, "Mai Anh slides a white sheet across with a sweet smile and offers a pen, and speaks; Linh takes the pen."),
     (8, 15, "Linh reads the sheet held low out of frame, one eyebrow lifting, and speaks innocently.")],
    [(3.4, 6.6, "Mai Anh", "speaking at a natural conversational pace, casual", "Chị ký giúp em vào phiếu tập phục hồi này nhé."),
     (8.5, 11.8, "Linh", "speaking slowly and softly with small natural pauses, innocent", "Phiếu tập gì mà có chỗ ghi… ly hôn?")],
    "birdsong, leaves rustling, slow breathing.")
json.dump(P, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fix2.json"), "w"), ensure_ascii=False, indent=1)
for k, v in P.items(): print(k, v[0], len(v[1]))
