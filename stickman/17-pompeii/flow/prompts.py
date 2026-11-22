# Flow prompts – Stickman tập 17 POMPEII. Same conventions as 10-the-chien-2/flow/prompts.py:
#   BG  = 16:9 background plates (NO people – stick figures are drawn by rig.mjs on top)
#   VEO = ~8 s motion clips used via clip(c, "kN", lt) in scenes.mjs
# Run: python3 prompts.py  -> all.json, setbg.js (BG) + veo.json (VEO)
import json

BG = (" Horizontal 16:9 background plate, stylized 3D animated-film render, semi-realistic textures, cinematic lighting,"
      " soft depth of field, NO people, NO characters, NO bodies, NO skeletons, no text, no letters, no logos, no symbols."
      " Keep the bottom quarter as open flat ground where characters will stand. Scene: ")

B = {
# --- 00/01 Thành phố dưới chân núi (trước 79) ---
'p01': "aerial view of the Roman town of Pompeii in 79 AD on the Bay of Naples, red tiled roofs, forum, city walls, harbour, behind it a single broad green cone-shaped mountain covered with vineyards (Mount Vesuvius before the eruption, no smoke), sunny late morning",
'p02': "a busy-looking but empty Roman street in Pompeii, large stepping stones across the road, cart ruts in the paving, shop fronts with open wooden shutters, ochre and red plastered walls with faint red painted brush strokes (no readable letters), warm sunlight",
'p03': "a Roman street-food counter (thermopolium) with a marble L-shaped counter holding sunken terracotta jars, colourful frescoes of ducks and a sea nymph on the counter front, amphorae on shelves, steam rising, warm light",
'p04': "a Roman bakery with large hourglass-shaped lava-stone grain mills and a domed brick oven glowing orange, round loaves on a wooden board, flour dust in the light",
'p05': "the forum of Pompeii with the Temple of Jupiter on a high podium, colonnades on both sides, and the green cone of Vesuvius rising behind the temple, blue sky",
'p06': "the stone amphitheatre of Pompeii seen from the arena floor, oval tiers of seats, canvas awning ropes, bright afternoon sun",
'p07': "terraced vineyards on the lower slopes of a green volcano above the Bay of Naples, grapes, small farmhouse, Roman merchant ships in the bay below",
'p08': "a Roman harbour warehouse stacked with clay amphorae of fish sauce and wine, wooden cranes, ropes, the sea beyond",
# --- 02 Những cơn rung (62–79) ---
'p09': "a Roman temple damaged by an earthquake, cracked columns, a fallen bronze statue lying on the steps, dust in the air, wooden props holding a wall",
'p10': "inside a Roman house under renovation, wooden scaffolding, a half-painted red fresco wall, buckets of fresh plaster and pigment pots, trowels, morning light",
'p11': "a green meadow at the foot of a volcano at dawn, a scattered flock of sheep lying still in low grey mist, eerie quiet mood, no blood",
'p12': "a stylized cutaway cross-section of a volcano showing glowing orange magma rising through a dark conduit beneath a green mountain and a small town, educational diagram look",
# --- 03 Đám mây hình cây thông ---
'p13': "the Roman naval base of Misenum, a harbour full of oared war galleys, a hillside villa with a terrace overlooking the bay, early afternoon",
'p14': "view from a villa terrace across the wide Bay of Naples toward a distant mountain erupting a gigantic vertical column of grey ash that spreads at the top like an umbrella pine tree, clear blue sky elsewhere",
'p15': "a single tall Mediterranean umbrella pine tree on a sunny hill, flat spreading crown, clear sky",
'p16': "view from very high altitude above the clouds, a colossal eruption column punching through into the dark blue stratosphere, curvature of the Earth on the horizon",
'p17': "a Roman study room with papyrus scrolls in pigeonholes, wax writing tablets, a bronze oil lamp, a window with afternoon light",
# --- 04 Trời tối giữa ban ngày ---
'p18': "a Pompeii street in eerie darkness at mid-afternoon, sky black-brown with ash, small grey-white pumice stones covering the road knee-deep, a single oil lamp glowing in a doorway",
'p19': "inside a Roman atrium with an open square roof hole, pumice stones pouring down through the opening into the shallow pool, dim lamp light, dust",
'p20': "a Roman city gate road leading out of town in darkness, an abandoned two-wheeled cart, pumice piled on the road, torch glow",
'p21': "a Roman room with a collapsed wooden roof, broken beams and red roof tiles lying on a heap of grey pumice, dim light",
# --- 05 Chuyến tàu của đô đốc ---
'p22': "a large Roman oared warship (quadrireme) on a rough dark sea, ash falling like grey snow, glowing volcano on the horizon",
'p23': "a coastline with the shallow water choked by a floating raft of grey pumice stones, waves, dark sky",
'p24': "a seaside Roman villa courtyard at night, ash and pumice piling up against the doors, torches flickering, sea in the background",
'p25': "a dark beach under a black sky with a sulphurous yellow haze, wild crashing waves, an old sail cloth spread on the sand",
# --- 06 Nửa đêm ở Herculaneum ---
'p26': "the small Roman seaside town of Herculaneum on a terrace above the beach, elegant villas and baths, evening, a dark ash cloud looming behind",
'p27': "a row of tall stone vaulted arches (Roman boat sheds) opening onto an ancient beach at night, wooden fishing boats pulled up on the sand, moonlight",
'p28': "at night, a glowing avalanche of hot ash and gas rolling down the slope of a volcano toward a coastal town, wide shot, orange and grey",
'p29': "the excavated ancient beach of Herculaneum today, a row of empty stone vaulted chambers at the base of a high cliff of solidified grey volcanic deposit, modern town above, daylight",
'p30': "a small Roman room with a wooden bed and a lamp niche, night, quiet",
# --- 07 Buổi sáng cuối cùng ---
'p31': "a Pompeii street at dawn buried up to the window sills in grey pumice, dark sky with a dull orange glow, eerie",
'p32': "the walls of Pompeii seen from outside, a towering grey ash cloud rolling toward them across the countryside at dawn",
'p33': "a dark coastal road at Misenum under thick falling ash, an overturned cart, scattered baskets, torches, total darkness except lamp light",
'p34': "a silent grey landscape after the eruption, everything covered in ash, a steaming smoking volcano with a broken summit, pale sun",
# --- 08 Thành phố bị lãng quên (79–1763) ---
'p35': "a grand Roman imperial hall with marble columns, purple drapes, a throne, scrolls on a table",
'p36': "the tops of ruined Roman walls and upper floors sticking out of a grey ash plain, makeshift wooden shelters and a small oven among them, poor camp, overcast",
'p37': "a grassy hill with vineyards, olive trees and sheep in the Italian countryside, 16th century, no ruins visible, peaceful",
'p38': "a 16th-century underground canal tunnel cutting through earth, its wall revealing a fragment of an ancient painted fresco, lantern light",
'p39': "an 18th-century excavation trench with ladders, wicker baskets, pickaxes and wheelbarrows, revealing Roman walls and a fresco, Vesuvius smoking in the background",
'p40': "a half-buried white marble inscription slab in an excavation pit (carved surface blank, no letters), sunlight",
# --- 09 Những khoảng trống trong tro (1863) ---
'p41': "a 19th-century excavation at Pompeii, a cut face of hardened grey ash showing a dark hollow cavity, buckets of white plaster, wooden funnels, ropes, sunlight",
'p42': "a museum room with empty glass display cases on plinths, soft gallery lighting, Roman frescoes on the walls",
'p43': "a quiet Roman garden courtyard (peristyle) with columns, plants and a fountain, restored ruins, afternoon light",
# --- 10 Những bí mật mới (2018–2024) ---
'p44': "a newly excavated room in Pompeii with a plastered wall bearing faint charcoal scribbles (no readable letters), archaeology tools, protective roof, soft daylight",
'p45': "a rustic still life on a wooden table: pomegranates, figs, walnuts, a bronze charcoal brazier and sealed clay wine jars",
'p46': "a modern ancient-DNA clean-room laboratory, white benches, sequencing machines, pipettes, blue light",
# --- 11 Thư viện hóa than ---
'p47': "a luxurious Roman seaside villa with a long colonnaded garden pool, bronze statues, view over the sea (Villa of the Papyri)",
'p48': "several carbonized ancient papyrus scrolls, black and charcoal-like, lying on dark velvet in a museum case, dramatic light",
'p49': "a huge particle accelerator synchrotron hall with a beamline, metal pipes, a small sample stage, blue and white light",
'p50': "a dark computer room with several monitors glowing with abstract grey 3D scans of a rolled scroll (no readable text)",
# --- 12 Núi lửa vẫn thức (1943–nay) ---
'p51': "Pompeii ruins at night in 1943, searchlight beams in the sky, smoke and a fire glow in the distance",
'p52': "a 1944 military airfield at the foot of an erupting volcano, rows of twin-engine WWII bombers covered with black ash, no markings, no insignia, lava glow at night",
'p53': "modern towns and dense apartment blocks sprawling up the slopes of Vesuvius, highways, sunset light, the crater on top",
'p54': "the Solfatara volcanic crater near Pozzuoli with white steaming fumaroles and yellow sulphur rocks, the bay in the distance",
'p55': "the forum of Pompeii today, ruined columns, Vesuvius with its twin-peaked modern profile in the background, sunny, empty",
'p56': "the edge of the Pompeii excavations, excavated walls next to a high green overgrown mound of unexcavated earth with trees",
'p57': "sunset over the Bay of Naples with the silhouette of Vesuvius, golden sky, calm sea",
'p58': "a dark smoky night sky lit from below by a volcanic orange glow, ash falling, dramatic (generic transition plate)",
}
ALL = {k: k + BG + v + "." for k, v in B.items()}

VEO_STYLE = (" 16:9, 8 seconds, stylized 3D animated-film render matching the background plates, cinematic lighting,"
             " NO people, NO characters, NO bodies, no text, no letters, no logos. Shot: ")
VEO = {
'k1':  "slow drone glide over the rooftops of Roman Pompeii in the morning toward a green mountain covered in vineyards, birds, smoke from bakery chimneys",
'k2':  "close-up of a Roman street-food counter, steam curling up from sunken terracotta jars, sunlight moving across frescoes",
'k3':  "earthquake: a Roman temple shakes, dust falls from cracked columns, a bronze statue topples off its base",
'k4':  "the summit of a green mountain explodes, a dark column of ash and pumice shoots straight up into the sky",
'k5':  "wide view across a bay: a giant ash column spreads at the top into an umbrella-pine shape, time-lapse feel, sea in the foreground",
'k6':  "grey-white pumice stones rain down on red-tiled roofs and a narrow street, piling up, light fading to darkness",
'k7':  "interior: a wooden roof beam cracks under the weight of pumice and collapses with tiles into a dark room, dust cloud",
'k8':  "a Roman oared warship rows hard through falling ash on a rough dark sea, oars splashing, volcano glowing behind",
'k9':  "the bow of a Roman ship pushes into a floating raft of grey pumice near the shore and slows down, waves",
'k10': "night, a villa courtyard slowly filling with ash, torches flickering, doors half blocked",
'k11': "night: the towering eruption column collapses and a glowing cloud of hot ash pours down the flank of the volcano",
'k12': "a glowing pyroclastic cloud races across a beach toward a row of stone boat-shed arches, everything turns grey",
'k13': "dawn: a grey wall of hot ash rolls over the city walls of Pompeii and swallows the streets",
'k14': "total darkness on a coastal road, oil lamps flicker, thick ash falling, distant lightning inside the ash cloud",
'k15': "aftermath: a silent grey ash landscape steaming under a pale sun, the volcano smoking quietly",
'k16': "time-lapse over centuries: grass, vines and trees grow over a grey mound where a city lies buried",
'k17': "18th-century: a pickaxe breaks through hardened earth, dust clears to reveal a colourful Roman fresco in lantern light",
'k18': "close-up: liquid white plaster is poured from a wooden funnel into a dark hole in hardened grey ash (no human shapes visible)",
'k19': "a soft brush sweeps dust off an ancient plastered wall revealing faint charcoal scribbles (no readable letters)",
'k20': "a carbonized black papyrus scroll slowly rotates inside an X-ray scanner, glowing blue scan lines",
'k21': "a 3D digital model of a rolled scroll virtually unrolls into a long flat sheet, glowing ink strokes appear (no readable letters)",
'k22': "night 1944: an erupting volcano with lava flows, hot ash and cinders rain down on parked WWII bombers with no markings",
'k23': "modern Naples at night with millions of city lights, slow push in toward the dark silhouette of Vesuvius",
'k24': "golden sunset over the ruins of Pompeii with Vesuvius behind, swallows flying, slow pull back",
}
VEO_ALL = {k: VEO_STYLE + v + "." for k, v in VEO.items()}

if __name__ == "__main__":
    json.dump(ALL, open('all.json', 'w'), indent=1, ensure_ascii=False)
    open('setbg.js', 'w').write("window.P=" + json.dumps(ALL) + ";window.__q=Object.keys(P);__q.length")
    json.dump(VEO_ALL, open('veo.json', 'w'), indent=1, ensure_ascii=False)
    print(len(ALL), "bg /", len(VEO_ALL), "veo")
