# Flow prompts – Stickman tập 18 ENDURANCE. BG = 16:9 background plates (NO people – stick figures drawn by rig.mjs on top)
# Run: python3 prompts.py -> all.json + setbg.js
import json
BG = (" Horizontal 16:9 background plate, stylized 3D animated-film render, semi-realistic textures, cinematic lighting,"
      " soft depth of field, NO people, NO characters, NO bodies, no text, no letters, no logos, no flags, no symbols."
      " Keep the bottom quarter as open flat ground or water where characters will be drawn. Scene: ")
B = {
# 00 / hook
'e01': "a wooden three-masted barquentine sailing ship (1912, black hull, no name) trapped and tilted in jagged Antarctic pack ice at polar twilight, pressure ridges of broken ice slabs against the hull, pink and violet sky",
'e02': "an endless flat white Antarctic ice floe under a pale pink and blue twilight sky, low sun on the horizon, scattered small icebergs, vast and lonely",
# 01 the dream
'e03': "an Edwardian London explorer's study in 1914, a large hand-drawn map of Antarctica pinned on the wall, a brass globe, a wooden desk with papers and an oil lamp, warm light",
'e04': "a Norwegian wooden shipyard in a fjord in 1912, a new black-hulled three-masted wooden ship on the slipway with scaffolding, snowy mountains, morning light",
'e05': "the stone quayside of Plymouth harbour in August 1914, a black wooden three-masted barquentine moored at the dock, crates and barrels, seagulls, summer morning",
# 02 into the ice
'e06': "the port of Buenos Aires in 1914 at sunset, warehouses, cranes, steamships and a wooden sailing ship at the dock, warm orange light",
'e07': "the Grytviken whaling station on South Georgia island in 1914, rusty red-roofed sheds, tall chimneys with steam, small whale-catcher steamboats in the harbour, snowy jagged mountains, cold blue light, no animals",
'e08': "the wooden deck of a 1914 polar expedition ship at sea, wooden dog kennel crates lashed along the rails, coiled ropes, masts and rigging, open blue ocean, sunny",
'e09': "the bow of a black wooden sailing ship pushing through loose Antarctic pack ice, narrow leads of dark blue water between white floes, small icebergs, bright low sun",
'e10': "a black wooden three-masted ship frozen solid in a flat endless plain of white pack ice, sails furled, calm, low golden sun, long blue shadows",
# 03 winter in the ice
'e11': "at night in the Antarctic winter, a wooden three-masted ship completely coated in white frost and ice, rigging glowing brilliant white in a harsh flash of light from the side, black sky, dramatic",
'e12': "the cosy interior of a wooden ship's wardroom converted to winter quarters in 1915, small wooden bunk cubicles, an iron stove, oil lamps, a long table with tin mugs, warm amber light",
'e13': "a row of small snow-block kennels (dog igloos) on the ice beside a frozen wooden ship at twilight, lanterns, snow drifts, no animals",
'e14': "green and pink aurora australis curtains over a frozen wooden three-masted ship in the polar night, stars, ice plain",
# 04 crushed
'e15': "huge pressure ridges of broken ice slabs piling up and pushing against the side of a black wooden ship that heels over, grey sky, snow spray, violent",
'e16': "a crushed wooden three-masted ship lying broken in the ice at dusk, masts snapped, rigging tangled, ice slabs piercing the hull, sad mood",
'e17': "inside the flooded dark hold of a wooden ship, icy black water, broken wooden beams, floating crates and wooden boxes, a shaft of dim light",
'e18': "a dark patch of open water among white pack ice where a ship has just sunk, a few floating planks, grey overcast sky, silent",
# 05 ocean camp
'e19': "a camp of five pale thin canvas tents on a flat ice floe at night, moonlight glowing through the thin tent fabric, three wooden lifeboats on sledges nearby, stars",
'e20': "a smoking blubber stove made from an oil drum on the ice with blackened cooking pots and a wooden crate table, camp kitchen, grey day",
'e21': "rough hummocky Antarctic pack ice with deep soft wet snow and cracks, flat grey overcast light, hard terrain",
# 06 patience camp
'e22': "a small cracked ice floe drifting on dark grey sea, open leads of water all around, distant snowy mountain peaks on the horizon, overcast",
'e23': "sea ice breaking apart at dusk, a wide crack of black water opening across a white floe, chunks of ice, tension",
# 07 three boats
'e24': "a stormy grey Southern Ocean among drifting ice floes, low dark clouds, spray, cold wind, wide shot",
'e25': "black dorsal fins of killer whales cutting through icy grey water between ice floes, mist",
'e26': "a narrow shingle beach below black rocky cliffs and a blue glacier on Elephant Island, crashing surf, gloomy grey sky",
# 08 elephant island
'e27': "a small bleak rocky spit on Elephant Island with a glacier behind, elephant seals and penguins on the stones, storm clouds, spray",
'e28': "a gigantic stormy ocean with enormous grey-green waves and white foam, Drake Passage, dramatic sky",
# 09 17 days
'e29': "night at sea, a colossal breaking wave with a long white crest high in the dark sky, moonlight, terrifying scale",
'e30': "black cliffs and glaciers of South Georgia island seen from rough sea, storm clouds, spray, a small cove",
'e31': "a small rocky cove on South Georgia with a shallow cave, tall tussock grass, a stream of fresh water running over boulders, calm after the storm",
# 10 crossing
'e32': "the jagged unmapped snowy mountains and glaciers of South Georgia under a bright full moon at night, crevasses, silver light",
'e33': "a long steep snow slope falling into fog at dusk on a mountain, vast and dangerous",
'e34': "Stromness whaling station seen from the hills at dawn, wooden sheds, chimneys with smoke, a harbour, mountains with zig-zag rock layers, first light",
# 11 rescue
'e35': "the cramped dim interior of a shelter made from two upturned wooden boats on rocks, sleeping bags, a blubber lamp, smoke, sail cloth walls",
'e36': "Elephant Island beach in winter, sea ice and brash ice filling the bay, fog, cold grey light",
'e37': "a small black steam tugboat emerging out of thick fog near an icy rocky coastline, grey sea, hopeful light breaking through",
# 12 the wreck
'e38': "a quiet whalers' cemetery at Grytviken with white wooden crosses and one granite headstone (blank, no text), tussock grass, snowy mountains, soft light",
'e39': "a modern red polar icebreaker research ship pushing through Antarctic sea ice with a helicopter deck, bright day, blue sky",
'e40': "the dark deep sea floor three kilometres down, a bright beam of light from an underwater robot cutting through floating marine snow, mysterious",
'e41': "the stern of an old wooden shipwreck standing upright on the deep sea floor, covered in pale sea anemones and sponges, lit by a single spotlight in total darkness, no letters",
# 13
'e42': "golden Antarctic sunset over icebergs and calm sea, peaceful, hopeful",
'e43': "a dark wooden ship wheel and an old brass sextant on a chart table, lamp light, close-up still life",
'e44': "the wild sea between Elephant Island and South Georgia, a tiny horizon, gloomy squalls, grey light",
}
allp = {k: BG + v + "." for k, v in B.items()}
json.dump(allp, open("all.json", "w"), ensure_ascii=False, indent=1)
open("setbg.js", "w").write("window.P=" + json.dumps({k: k + " " + v for k, v in allp.items()}, ensure_ascii=False) + ";")
print(len(allp))
