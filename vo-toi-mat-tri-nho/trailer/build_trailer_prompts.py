#!/usr/bin/env python3
"""Prompt trailer theo "giọng A" (kiểu Cái Kết Cho Tiểu Tam): clip nhiều shot, hội thoại liền, giọng do câu tả cố định quyết định."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_v2"))
from looks import FACE, NAME, ROLE, LOOKS, PLACE, VOICE  # noqa: E402

STYLE = ("Photorealistic live-action Vietnamese romantic comedy-drama with a thriller edge, shot on ARRI Alexa 35 with anamorphic lenses, "
         "24 fps; rich teal-and-amber grade, motivated practical light, natural skin texture with pores, subtle 35mm film grain, shallow depth of field "
         "with creamy oval bokeh, gentle halation. Real actors, believable understated performances, a premium theatrical feature — never CGI, never an advertisement.")
AVOID = ("On-screen text of any kind (subtitles, captions, titles, watermarks, logos), readable writing, blurry faces, distorted hands, background music, "
         "letterbox bars, cuts at any other moment, extra people in focus, face, hair or costume changes, robotic or text-to-speech sounding voices, "
         "flat monotone delivery, slurred speech, repeated, stuttered or echoed words, the line spoken twice, an off-screen narrator or voice-over, "
         "Southern or Central Vietnamese accents.")

def char_line(code):
    who, flow, outfit = LOOKS[code]
    return f"- @{who} = {NAME[who]}, {ROLE[who]}: {FACE[who]}; wears {outfit}. Attached image: \"{flow}\"."

def build(c):
    cuts = ", ".join(f"{s}s" for s in c["cuts"])
    L = [f"A {c['dur']}-second live-action film sequence of {len(c['shots'])} shots, 16:9 widescreen, 24 fps, with hard cuts only at {cuts}; "
         "one place and one moment, sound and action continuous across the cuts.", "",
         "[STYLE]", STYLE, "", "[LOCATION]", PLACE[c["loc"]][1][0].upper() + PLACE[c["loc"]][1][1:] + ".", "",
         "[CHARACTERS]",
         "Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, "
         "and never flash the studio reference portrait; the characters are already in place in the very first frame."]
    L += [char_line(x) for x in c["looks"]]
    L += ["Nobody else appears in focus.", "", "[SHOT LIST — hard cuts only at the marked seconds]"]
    L += [f"- Shot {i}, {a}–{b}s: {d}" for i, (a, b, d) in enumerate(c["shots"], 1)]
    L += ["- Whoever is speaking has the face clearly on screen in that shot; the camera keeps one side of the line so eyelines match across the cuts.", "",
          "[TIMELINE — second by second]", "Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per beat."]
    L += [f"- {t}" for t in c["timeline"]]
    turns = c["turns"]
    L += ["", "[AUDIO]"]
    if turns:
        L.append(f"- Dialogue in Vietnamese with exact lip-sync, {len(turns)} spoken turn{'s' if len(turns) > 1 else ''} in this order, each said exactly once (no subtitles):")
        for i, (who, a, b, how, line) in enumerate(turns, 1):
            L.append(f"- Turn {i}, {a}–{b}s, spoken on camera by @{who} ({VOICE[who]}, {how}): \"{line}\"")
        end = max(t[2] for t in turns)
        L += ["- Throughout, only the person whose turn it is moves the lips while anyone else listens with the mouth closed; real breaths and tiny natural "
              "hesitations, recorded close on set with a little room tone — it sounds like real actors talking, never like a voice-over or text-to-speech.",
              "- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, "
              "and different characters sound clearly different in pitch, age and texture.",
              f"- All speech is over by {end}s. From then until {c['dur']}.0s nobody says a word; no line is ever repeated to fill the time.",
              "- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud."]
    else:
        L.append("- No dialogue: every mouth stays closed, no voices at all.")
    L += [f"- SFX: {c['sfx']}. No music.", "", "[AVOID]", AVOID]
    return "\n".join(L) + "\n"

CLIPS = [
 dict(id="T1", title="Cột ở sảnh", dur=12, cuts=[4, 7, 10], loc="B2", looks=["L1", "Q1"],
      shots=[(0, 4, "35mm medium-wide shot as the wife steps out of the brass elevator into the lobby, slow push-in."),
             (4, 7, "85mm close-up of the husband beside a marble pillar, a flash of a white dress hem vanishing behind it, locked off."),
             (7, 10, "85mm close-up of the wife, a slow push-in as her eyes flutter."),
             (10, 12, "35mm wide shot as she sinks onto an emerald velvet sofa, slow crane-down.")],
      timeline=["0–1s (Shot 1): @Linh steps out of the brass elevator, perfectly calm, already speaking softly.",
                "1–4s (Shot 1): @Linh keeps speaking evenly as she walks toward the camera, eyes fixed on a marble pillar.",
                "4–7s (CUT to Shot 2): @Quan, sweating, spreads his hands and blurts his answer with a nervous laugh.",
                "7–10s (CUT to Shot 3): @Linh looks at him in silence; her eyes flutter, her lips part, she sways. Mouth closed.",
                "10–12s (CUT to Shot 4): @Linh collapses gracefully onto the velvet sofa, the gown pooling; @Quan lunges to catch her, mouth closed. The sequence settles on this as its final frame."],
      turns=[("Linh", 0.6, 3.6, "speaking slowly and softly, polite and lethal", "Cô ấy đứng sau cái cột kia, phải không anh?"),
             ("Quan", 4.3, 6.6, "speaking quickly, flustered, a nervous laugh in the breath", "Khách sạn này… toàn cột thôi em ạ!")],
      sfx="the hush of a grand lobby, a soft elevator chime, heels on marble, a gasp and the soft thump of the body landing on velvet"),
 dict(id="T2", title="Anh là ai?", dur=12, cuts=[4, 7, 10], loc="B3", looks=["L2", "Q1"],
      shots=[(0, 4, "100mm macro on the wife's closed eyes opening, then rack focus to the husband holding her hand."),
             (4, 7, "85mm close-up of the wife on the pillow, locked off."),
             (7, 10, "50mm medium two-shot by the bed, subtle handheld."),
             (10, 12, "85mm close-up of the husband, slow push-in.")],
      timeline=["0–4s (Shot 1): @Linh's eyes slowly open; @Quan leans in, holding her hand, relieved. Mouths closed.",
                "4–7s (CUT to Shot 2): @Linh looks at him blankly and asks one small question.",
                "7–10s (CUT to Shot 3): @Linh yanks her hand away and sits bolt upright, outraged, and snaps at him.",
                "10–12s (CUT to Shot 4): @Quan freezes, jaw dropped, speechless, mouth hanging open. The sequence settles on this as its final frame."],
      turns=[("Linh", 4.4, 5.9, "speaking slowly, small and puzzled", "Anh… là ai?"),
             ("Linh", 7.3, 9.8, "speaking quickly, outraged and indignant", "Bỏ ra! Tôi còn chưa có người yêu!")],
      sfx="a soft monitor beep, rustling hospital sheets, distant hallway murmur"),
 dict(id="T3", title="Bác sĩ đồng phạm", dur=10, cuts=[3, 6], loc="B3", looks=["L2", "K1"],
      shots=[(0, 3, "35mm medium shot of the wife lying still in bed as the door clicks shut, locked off."),
             (3, 6, "85mm close-up of the wife opening one eye, locked off."),
             (6, 10, "50mm medium two-shot: the doctor at the foot of the bed, the wife sitting up, slow push-in.")],
      timeline=["0–3s (Shot 1): the door clicks shut off-screen; @Linh lies perfectly still, eyes closed, mouth closed.",
                "3–6s (CUT to Shot 2): @Linh opens one eye, glances at the door and whispers.",
                "6–9s (CUT to Shot 3): @Khang folds his arms, utterly deadpan, and answers dryly.",
                "9–10s (Shot 3): @Linh sits up with a mischievous grin, mouth closed. The sequence settles on this as its final frame."],
      turns=[("Linh", 3.4, 4.3, "a sly whisper", "Đi chưa?"),
             ("Khang", 6.4, 8.6, "speaking slowly, deadpan and dry", "Diễn viên xuất sắc nhất năm.")],
      sfx="a door latch clicking shut, a soft monitor beep, a quiet hospital hum"),
 dict(id="T4", title="Phó tổng dưới mưa", dur=10, cuts=[4], loc="B6", looks=["H1"],
      shots=[(0, 4, "35mm medium shot of the man at the gate under a black umbrella in the drizzle, slow push-in."),
             (4, 10, "85mm close-up of his face under the umbrella, rain streaks in the lamp light, locked off.")],
      timeline=["0–4s (Shot 1): @Hung stands at the wrought-iron gate under his black umbrella, looking straight past the camera, and speaks softly.",
                "4–8s (CUT to Shot 2): @Hung tilts his head and continues, polite and cold.",
                "8–10s (Shot 2): a thin smile that never reaches his eyes; mouth closed. The sequence settles on this as its final frame."],
      turns=[("Hung", 0.6, 3.3, "speaking slowly and quietly, mock-sympathetic", "Nghe nói vợ chú mất trí nhớ?"),
             ("Hung", 4.5, 8.2, "speaking slowly, every word a polite threat", "Tiếc thật. Quỹ Hoa Anh Đào rất coi trọng gia đình.")],
      sfx="fine rain pattering on the umbrella, dripping iron bars, a far-off car passing on wet asphalt"),
 dict(id="T5", title="Chiếc váy trắng", dur=10, cuts=[3, 8], loc="B9", looks=["L4", "M2"],
      shots=[(0, 3, "100mm macro insert: a woman's fingers slowly draw a white dress hem out of a gym bag, slow push-in."),
             (3, 8, "50mm medium close-up of the wife, sweet smile, subtle handheld."),
             (8, 10, "85mm close-up of the young woman, locked off.")],
      timeline=["0–3s (Shot 1): @Linh's fingers pull a white bouclé dress out of a sports bag on the console. No one speaks.",
                "3–8s (CUT to Shot 2): @Linh holds the dress up against the young woman's shoulder and says, sweetly, the knife hidden in the smile.",
                "8–10s (CUT to Shot 3): @MaiAnh's face drains pale; a frozen, forced smile; she swallows, mouth closed. The sequence settles on this as its final frame."],
      turns=[("Linh", 3.4, 7.6, "speaking slowly and sweetly, light and deadly", "Váy đẹp đấy. Hôm trước tôi thấy một cái y hệt… ở sảnh khách sạn.")],
      sfx="morning birds outside, the zip of a sports bag, fabric rustling, a tense swallow"),
 dict(id="T6", title="Đêm mưa", dur=10, cuts=[4, 7], loc="B19", looks=["M4", "Q2"],
      shots=[(0, 4, "50mm medium shot of the young woman soaked in the doorway, rain behind her, locked off."),
             (4, 7, "85mm close-up of the husband, slow push-in."),
             (7, 10, "35mm medium shot toward the rain-streaked dark window, then the husband turns, subtle handheld.")],
      timeline=["0–4s (Shot 1): @MaiAnh stands dripping in the kitchen doorway, hair plastered to her face, and says quietly, trembling.",
                "4–7s (CUT to Shot 2): @Quan, in rumpled pyjamas, takes one step back, stunned. Mouth closed.",
                "7–8s (CUT to Shot 3): a hard white camera flash bursts outside the dark window.",
                "8–10s (Shot 3): @Quan spins toward the window — only rain streaming down the glass. Mouth closed. The sequence settles on this as its final frame."],
      turns=[("MaiAnh", 0.8, 2.9, "speaking softly, shivering, small and shaky", "Em không đi đâu nữa.")],
      sfx="heavy rain on the windows, a dripping coat, a steaming pot, the sharp click of a camera shutter outside"),
 dict(id="T7", title="Chủ tịch", dur=15, cuts=[4, 6, 10, 12], loc="B22", looks=["H2", "L9"],
      shots=[(0, 4, "50mm medium shot of the vice president at the glowing projector screen, slow push-in."),
             (4, 6, "100mm low insert of red stiletto heels striding through the opening glass doors."),
             (6, 10, "35mm low-angle medium shot of the wife walking in, the room light warming around her, steady tracking."),
             (10, 12, "85mm close-up of the vice president, locked off."),
             (12, 15, "85mm close-up of the wife, slow push-in.")],
      timeline=["0–4s (Shot 1): @Hung gestures at the blank glowing screen and announces, smooth and triumphant.",
                "4–6s (CUT to Shot 2): the glass doors swing open; red heels click in. No one speaks.",
                "6–10s (CUT to Shot 3): @Linh walks in, white power suit, cherry-blossom hairpin, and speaks to someone off-screen with a calm smile.",
                "10–12s (CUT to Shot 4): @Hung's smile cracks; he points at her and blurts out.",
                "12–14s (CUT to Shot 5): @Linh tilts her head and answers with two quiet words and a tiny smile.",
                "14–15s (Shot 5): silence, mouth closed, eyes steady. The sequence settles on this as its final frame."],
      turns=[("Hung", 0.4, 3.8, "speaking smoothly, triumphant, savouring every word", "Giám đốc ngoại tình. Vợ mất trí. Hoa Anh Đào sẽ rút vốn."),
             ("Linh", 6.5, 9.4, "speaking slowly and calmly, warm with a sting", "Anh Quân. Anh vừa qua vòng phỏng vấn."),
             ("Hung", 10.2, 11.7, "speaking fast, cracking, disbelieving", "Bà ấy… mất trí nhớ!"),
             ("Linh", 12.4, 13.6, "speaking softly, amused, final", "Có chọn lọc.")],
      sfx="a projector fan hum, glass doors swinging open, sharp heel clicks on stone, a stunned murmur"),
 dict(id="T8", title="Hợp đồng làm chồng", dur=10, cuts=[4, 8], loc="B24", looks=["Q5", "L10"],
      shots=[(0, 4, "35mm medium-wide shot: the husband kneeling under the white rose arch with an open ring box, slow push-in."),
             (4, 8, "50mm medium close-up of the wife holding up a thin contract, sweet smile, locked off."),
             (8, 10, "85mm close-up of the husband, subtle handheld.")],
      timeline=["0–4s (Shot 1): @Quan kneels under the rose arch, ring box open, and begins his speech, hopeful.",
                "4–8s (CUT to Shot 2): @Linh holds up a thin contract between two fingers and states her terms sweetly.",
                "8–10s (CUT to Shot 3): @Quan gulps and nods far too fast, mouth closed. The sequence settles on this as its final frame."],
      turns=[("Quan", 0.6, 2.8, "speaking slowly and tenderly, a little nervous", "Cô gái hai mươi hai tuổi ơi…"),
             ("Linh", 4.4, 7.6, "speaking sweetly and calmly, a playful threat", "Vi phạm thì anh mất trí nhớ. Lần này là thật.")],
      sfx="crickets, the soft crackle of candles, fairy lights tinkling in the breeze, distant laughter"),
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
    os.makedirs(out, exist_ok=True)
    for c in CLIPS:
        for who, a, b, how, line in c["turns"]:
            assert b <= c["dur"] - 0.8, (c["id"], line)
        open(os.path.join(out, f"{c['id']}.txt"), "w", encoding="utf-8").write(build(c))
        print(c["id"], c["dur"], "s", c["looks"], len(build(c)))
