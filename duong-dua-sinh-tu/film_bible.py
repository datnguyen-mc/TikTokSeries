#!/usr/bin/env python3
"""Global Film Bible & State Resolution Engine for Google Flow Omni Filmmaking.

Provides a single source of truth (`GLOBAL_FILM_BIBLE`) for:
1. CHARACTER_LOCK: Identity, face, body, hairstyle, costume variants, voice, and personality.
2. VEHICLE_LOCK: Vehicle ID, model/silhouette, color/material, dimensions, wheels/axles,
   lights/accessories, interior layout, left-hand steering position, driver/passenger assignments,
   and scene-indexed mechanical/damage state.
3. ENVIRONMENT_LOCK: Recurring locations, architecture, road/lane geometry, terrain/landmarks,
   interior furniture, weather/atmosphere, time-of-day lighting, 180-degree camera axis, and sound.
4. OBJECT_LOCK: Persistent props, equipment, ownership, hand placement, and state progression.
5. PHYSICS_RULES: Context-selective realistic vehicle, human, object, and environmental physics.
6. CINEMATIC_STYLE: Visual style, color grading, frame rate, aspect ratio, and camera setups.
7. AUDIO_STYLE: Southern Vietnamese speech, narrator lock, supporting voices, and diegetic sound.
8. OMNI_MODEL_CAPABILITIES: Google Flow Omni workflow profiles (`text_to_video`, `ingredients_r2v`,
   `frame_i2v`, `insert_shot`, `video_extend`, `video_edit`).
"""
from __future__ import annotations

from typing import Any

CHARACTER_LOCK: dict[str, dict[str, Any]] = {
    "TOM": {
        "id": "TOM",
        "tag": "@Tom",
        "name": "Tom",
        "media_id": "53e825dd-52eb-41f9-bf6a-4fe562792c55",
        "age": 27,
        "face": "sharp observant dark eyes, faint small scar at outer left eyebrow, clean square jawline",
        "body": "183 cm, athletic lean build, balanced posture",
        "hairstyle": "short textured sandy-dark hair",
        "identity": "Young Vietnamese-American man, athletic lean build, sharp observant dark eyes, short textured dark-brown hair, clean jawline",
        "voice": "low, calm, clear Southern Vietnamese male voice",
        "personality": "disciplined undercover LAPD officer, observant under pressure, torn between badge and brotherhood",
        "costumes": {
            "TOM": "fitted charcoal T-shirt under an open dark-blue denim work shirt, oil-scuffed dark jeans, worn brown work boots, steel chronograph watch on left wrist",
            "TOM_R": "matte-black leather bomber jacket over a grey crew-neck T-shirt, dark jeans, black driving sneakers, steel chronograph watch on left wrist",
            "TOM_B": "open dark-blue work shirt over charcoal T-shirt, light dust smudge on jaw from stunt training, dark jeans, worn work boots",
        },
    },
    "MICDO": {
        "id": "MICDO",
        "tag": "@Micdo",
        "name": "Micdo",
        "media_id": "0044e498-ba46-4b33-b325-cb5a322cf73a",
        "age": 32,
        "face": "commanding deep-set dark eyes, strong square jawline, weathered calm brow",
        "body": "185 cm, muscular heavy-shouldered build, grounded stance",
        "hairstyle": "clean-shaven bald head",
        "identity": "Muscular man with a shaved head, commanding dark eyes, strong jawline, silver cross pendant on a heavy neck chain",
        "voice": "deep, resonant, authoritative Southern Vietnamese male voice",
        "personality": "commanding street-racing leader, fiercely protective of his family, calm until crossed",
        "costumes": {
            "MICDO": "fitted white sleeveless tank top under an open black leather jacket, silver cross pendant on chain, dark jeans, heavy black boots",
            "MICDO_H": "black tactical driving windbreaker zipped over dark shirt, black leather driving gloves, dark cargo trousers, heavy boots",
            "MICDO_W": "scuffed black leather jacket over white tank top, light dust smudge on forehead after the stunt spin, bare hands, dark jeans, heavy boots",
        },
    },
    "AMI": {
        "id": "AMI",
        "tag": "@Ami",
        "name": "Ami",
        "media_id": "7226ddde-c39f-4278-a8ed-ab6187fb7509",
        "age": 24,
        "face": "warm olive skin, expressive dark eyes, natural brows, silver stud earrings",
        "body": "168 cm, slim athletic build, poised natural movement",
        "hairstyle": "long dark-brown hair tied half-back",
        "identity": "Young woman with warm olive skin, expressive dark eyes, long dark-brown hair tied half-back, silver stud earrings",
        "voice": "warm, clear, expressive Southern Vietnamese female voice",
        "personality": "perceptive heart of the Toto family diner, candid, loyal, emotionally direct",
        "costumes": {
            "AMI": "fitted burgundy scoop-neck top, light-wash jeans, canvas shop apron tied at the waist, flat sneakers, silver stud earrings",
            "AMI_N": "cropped tan suede jacket over burgundy top, dark jeans, sneakers, hair loose over shoulders",
        },
    },
    "CEVIN": {
        "id": "CEVIN",
        "tag": "@Cevin",
        "name": "Cevin",
        "media_id": "a0c490db-9269-4093-b7d6-54c7f854dca5",
        "age": 29,
        "face": "intense brow, neat goatee, small chin scar",
        "body": "179 cm, wiry muscular build, coiled restless posture",
        "hairstyle": "short spiky bleached-tip dark hair",
        "identity": "Athletic man with short spiky bleached-tip hair, intense brow, faint scar on right knuckle, silver chain bracelet on right wrist",
        "voice": "rough, fiery, direct Southern Vietnamese male voice",
        "personality": "hot-headed lieutenant, fearless in high-speed cable stunts, fiercely territorial",
        "costumes": {
            "CEVIN": "maroon short-sleeve mechanic shirt with rolled sleeves, silver chain bracelet on right wrist, dark cargo jeans, work boots",
            "CEVIN_H": "black hooded tactical vest over dark long-sleeve shirt, fingerless driving gloves, safety harness clip at waist, dark cargo pants",
            "CEVIN_W": "scuffed black tactical vest with a clean folded towel held against his waist harness after the high-speed stunt, sweat-streaked face, fingerless gloves",
        },
    },
    "CINA": {
        "id": "CINA",
        "tag": "@Cina",
        "name": "Cina",
        "media_id": "6ef4b4a9-e0a5-4b63-a245-a995f11bd7ea",
        "age": 28,
        "face": "sharp jawline, fierce confident dark gaze, small hoop earring in left ear",
        "body": "167 cm, lean athletic build, precise agile hands",
        "hairstyle": "short tousled chin-length black hair",
        "identity": "Lean athletic woman with short tousled black hair, fierce confident gaze, small hoop earring in left ear",
        "voice": "cool, firm, clear Southern Vietnamese female voice",
        "personality": "composed precision driver and mechanic, unflinching under highway pressure",
        "costumes": {
            "CINA": "cropped black leather vest over crimson top, low-rise dark leather trousers, heavy lace boots",
            "CINA_H": "fitted black zip driving jacket, fingerless leather driving gloves, dark tactical pants, compact radio earpiece",
        },
    },
    "SEJA": {
        "id": "SEJA",
        "tag": "@Seja",
        "name": "Seja",
        "media_id": "7dc7e4cc-d7ae-47e4-b3d3-cee720775859",
        "age": 22,
        "face": "quick restless eyes, thin-framed technical glasses, earnest expression",
        "body": "175 cm, wiry lanky build, quick kinetic hand gestures",
        "hairstyle": "messy curly dark hair",
        "identity": "Wiry young man with messy curly dark hair, quick restless eyes, thin-framed technical glasses",
        "voice": "quick, earnest, energetic Southern Vietnamese male voice",
        "personality": "brilliant ECU and telemetry prodigy, anxious when out of his depth, eager to prove himself",
        "costumes": {
            "SEJA": "oversized olive graphic work shirt over striped long-sleeve tee, cargo trousers, sneakers, canvas laptop strap across chest",
            "SEJA_R": "white-and-blue racing windbreaker over dark tee, cargo trousers, driving shoes, thin-framed glasses",
        },
    },
    "ONLE": {
        "id": "ONLE",
        "tag": "@Onle",
        "name": "Onle",
        "media_id": "58d0ebc5-cd00-4af2-9ea8-3b11f352556e",
        "age": 30,
        "face": "neat goatee, calm steady dark eyes, composed expression",
        "body": "182 cm, broad-shouldered mechanic build, grease-weathered hands",
        "hairstyle": "closely cropped dark hair",
        "identity": "Broad-shouldered mechanic with a neat goatee, calm steady eyes, grease-weathered hands",
        "voice": "steady, grounded Southern Vietnamese male voice",
        "personality": "veteran chassis builder and tactical communications anchor, level-headed",
        "costumes": {
            "ONLE": "grease-stained dark-green mechanic jumpsuit tied at the waist over a black T-shirt, heavy work boots",
            "ONLE_H": "dark matte bomber jacket, black cap pulled low, dark jeans, leather driving gloves",
        },
    },
    "NYTRAN": {
        "id": "NYTRAN",
        "tag": "@NyTran",
        "name": "Ny Tran",
        "media_id": "3004cbee-ba9f-42d8-b11e-c55fec49e5ab",
        "age": 30,
        "face": "sharp cheekbones, cold calculating dark eyes, thin gold neck chain",
        "body": "177 cm, lean sharp build, upright predatory posture",
        "hairstyle": "sleek undercut slicked-back black hair",
        "identity": "Vietnamese man with sharp cheekbones, sleek undercut black hair, cold calculating eyes, gold neck chain",
        "voice": "cold, smooth, menacing Southern Vietnamese male voice",
        "personality": "ruthless Little Saigon syndicate boss, controlled, status-obsessed",
        "costumes": {
            "NYTRAN": "tailored black snake-pattern leather jacket over open-collar crimson silk shirt, gold chain, black trousers, polished boots",
            "NYTRAN_R": "armored black motorcycle leather jacket over crimson shirt, black riding gloves, dark trousers, riding boots",
        },
    },
    "CELA": {
        "id": "CELA",
        "tag": "@Cela",
        "name": "Cela",
        "media_id": "57d9ea23-b1c8-4f65-b65b-918d070bd76c",
        "age": 31,
        "face": "narrow watchful eyes, diagonal scar across right cheek",
        "body": "174 cm, compact muscular build, dragon tattoo sleeve on right forearm",
        "hairstyle": "shaved sides with a tied short topknot",
        "identity": "Wiry Vietnamese man with shaved sides and a tied topknot, narrow eyes, dragon tattoo sleeve on right forearm",
        "voice": "raspy, clipped Southern Vietnamese male voice",
        "personality": "Ny Tran's cousin and enforcer, aggressive, watchful",
        "costumes": {
            "CELA": "sleeveless black leather vest over dark shirt, dragon tattoo sleeve on right forearm, black jeans, riding boots",
        },
    },
    "NESE": {
        "id": "NESE",
        "tag": "@Nese",
        "name": "Nese",
        "media_id": "27ede5a3-d368-4b6e-a8e0-b8b4d8574f03",
        "age": 46,
        "face": "weathered lined face, stern focused eyes, trimmed moustache",
        "body": "180 cm, solid veteran build",
        "hairstyle": "greying crew-cut hair",
        "identity": "Veteran police sergeant with greying crew-cut hair, weathered lined face, stern focused eyes",
        "voice": "measured, seasoned Southern Vietnamese male voice",
        "personality": "pragmatic LAPD sergeant who understands the moral cost of undercover work",
        "costumes": {
            "NESE": "rolled-sleeve white dress shirt with loosened dark tie, badge holder at belt, charcoal trousers, leather shoes",
            "NESE_T": "dark navy police windbreaker over dress shirt, tactical vest, radio handset clipped at shoulder",
        },
    },
    "KINAN": {
        "id": "KINAN",
        "tag": "@Kinan",
        "name": "Kinan",
        "media_id": "c5238e27-22b2-44e2-84b7-a0b6296d649d",
        "age": 44,
        "face": "sharp angular features, piercing gaze, thin metal-frame glasses",
        "body": "178 cm, trim upright build",
        "hairstyle": "neatly parted dark-brown hair",
        "identity": "Tall federal agent with neatly parted dark hair, sharp angular features, piercing gaze",
        "voice": "crisp, urgent, commanding Southern Vietnamese male voice",
        "personality": "impatient FBI task-force commander focused on hard deadlines and arrests",
        "costumes": {
            "KINAN": "tailored dark charcoal suit over steel-blue shirt without tie, federal credential folder at side",
            "KINAN_T": "dark field windbreaker over steel-blue shirt, tactical vest, ear-tube radio",
        },
    },
    "VERNI": {
        "id": "VERNI",
        "tag": "@Verni",
        "name": "Verni",
        "media_id": "5e834823-4e0f-4c3c-a881-c645630a898a",
        "age": 48,
        "face": "thick grey-streaked beard, sun-weathered face, defiant eyes",
        "body": "173 cm, stocky barrel-chested build, strong forearms",
        "hairstyle": "receding hair under a worn trucker cap",
        "identity": "Stocky long-haul truck driver with a thick grey-streaked beard, sun-weathered face, strong forearms",
        "voice": "gravelly, booming Southern Vietnamese male voice",
        "personality": "hardened long-haul trucker determined to defend his rig on the highway",
        "costumes": {
            "VERNI": "plaid flannel shirt under a padded brown work vest, trucker cap, dark jeans, heavy boots",
        },
    },
}

VEHICLE_LOCK: dict[str, dict[str, Any]] = {
    "RIG_18": {
        "vehicle_id": "RIG_18",
        "name": "the 18-Wheel Charcoal Semi-Truck & Silver Trailer",
        "vehicle_type": "heavy long-haul semi-tractor coupled to a 53-foot box trailer",
        "model_silhouette": "conventional long-nose cab-behind-engine highway tractor with twin vertical chrome exhaust stacks and rectangular aluminum cargo trailer",
        "exterior_color_material": "deep industrial charcoal cab with brushed chrome grille and bumper; ribbed matte-silver aluminum trailer with rear double doors",
        "dimensions_proportions": "22 m total length, 4.1 m height, high cab side windows 2.4 m above asphalt",
        "wheels_axles": "18 wheels across 5 axles (2 front steering wheels, 8 dual drive wheels on tractor, 8 dual tandem wheels on trailer), heavy steel rims",
        "lights_accessories": "rectangular halogen headlights, amber roof marker lamps along cab and trailer top, wide dual west-coast side mirrors",
        "interior_layout": "LEFT-HAND DRIVE (US standard): high air-ride leather driver seat on the left, large 18-inch steering wheel, amber analog gauge cluster, manual gear lever at center, passenger door and window on the right",
        "steering_side": "LEFT",
        "default_driver": "VERNI",
        "default_passengers": [],
        "description": "Massive 18-wheel charcoal highway semi-truck and sealed silver cargo trailer hauling high-value electronics crates.",
        "damage_states": [
            ((1, 1), (1, 6), "intact sealed trailer doors, cruising steady at 110 km/h in center lane"),
            ((2, 1), (2, 6), "pneumatic grapnel cable anchored into right passenger window frame at highway speed"),
            ((3, 1), (3, 6), "rear trailer latch released by magnetic module, double doors swung open against highway slipstream"),
            ((4, 1), (4, 6), "rear trailer doors open as black Civic coupes disengage and peel off onto exit ramp"),
            ((32, 1), (34, 6), "steel cable hooked to right cab side while swerving across desert highway lanes"),
        ],
    },
    "CIVIC_TRIO": {
        "vehicle_id": "CIVIC_TRIO",
        "name": "the Three Matte-Black Precision Coupes",
        "vehicle_type": "three identical lowered 2-door sport-compact coupes",
        "model_silhouette": "low-slung 1990s aerodynamic 2-door coupe silhouette with sunroof hatch and low rear wing",
        "exterior_color_material": "non-reflective matte-black paint with dark-tinted side glass",
        "dimensions_proportions": "4.4 m length, 1.35 m low ride height, wide track stance",
        "wheels_axles": "4 wheels on 2 axles per coupe, 17-inch gunmetal 6-spoke alloy rims with low-profile street tires",
        "lights_accessories": "sharp projector headlights, continuous emerald-green LED underglow beneath side skirts and bumpers, openable sunroof hatch, reinforced front hood latches",
        "interior_layout": "LEFT-HAND DRIVE: driver seat on the left, compact sport steering wheel, green dashboard illumination, sunroof opening above front cabin",
        "steering_side": "LEFT",
        "default_driver": "MICDO",
        "default_passengers": ["CEVIN", "CINA", "ONLE"],
        "description": "Three matte-black lowered sport coupes with glowing green LED underglow, sunroof hatch and reinforced front hood latches.",
        "damage_states": [
            ((1, 1), (3, 6), "all three matte-black coupes intact with emerald-green underglow active in formation around the semi-truck"),
            ((4, 1), (4, 6), "all three coupes intact; green underglow switched off at clip 6 as they slip onto the dark exit ramp"),
            ((32, 1), (32, 6), "three matte-black coupes flanking the semi-truck in daylight on the desert highway"),
            ((33, 1), (33, 6), "Cina's #2 matte-black coupe suffers a deflated front-left tire from trailer contact and slides onto the sandy shoulder"),
        ],
    },
    "ECLIPSE": {
        "vehicle_id": "ECLIPSE",
        "name": "the Neon-Green Turbo Sport Coupe",
        "vehicle_type": "2-door turbocharged street-racing sport coupe",
        "model_silhouette": "curved aerodynamic wedge coupe with low front splitter, carbon-fiber hood, and dual-plane rear wing",
        "exterior_color_material": "glossy neon-lime green paint with matte weave carbon-fiber hood and subtle silver side streak graphics",
        "dimensions_proportions": "4.38 m length, 1.32 m height, lowered coilover stance",
        "wheels_axles": "4 wheels on 2 axles, 18-inch polished 5-spoke alloy wheels with low-profile performance tires",
        "lights_accessories": "sleek smoked projector headlights, blue cockpit gauge glow, twin blue NOS cylinders mounted in rear hatch",
        "interior_layout": "LEFT-HAND DRIVE: Sparco-style bucket seat on the left, 3-spoke sport wheel with red right-thumb NOS button, passenger telemetry laptop mount on the right dash",
        "steering_side": "LEFT",
        "default_driver": "TOM",
        "default_passengers": [],
        "description": "Neon-green tuned sport coupe with carbon hood, silver sport graphics, dual NOS bottles in the rear mount and telemetry laptop on the dash.",
        "damage_states": [
            ((5, 1), (14, 5), "pristine neon-green bodywork and carbon-fiber hood, twin NOS bottles pressurized in rear mount"),
            ((14, 6), (15, 1), "stage-1 NOS engaged at full boost, intake manifold running hot under redline load, exterior bodywork intact"),
            ((15, 2), (18, 6), "over-boosted intake manifold steaming lightly, passenger-side metal floor panel unlatched from high-speed friction sparks, minor front bumper rub mark"),
            ((19, 1), (19, 1), "parked in the Little Saigon gravel lot with rear nitrous pressure valves opened and venting vapor"),
            ((19, 2), (20, 6), "disabled in the Little Saigon gravel lot surrounded by dense theatrical orange smoke and a darkened scorched hood frame"),
        ],
    },
    "RX7": {
        "vehicle_id": "RX7",
        "name": "the Deep-Red Twin-Turbo Rotary Coupe",
        "vehicle_type": "2-door twin-turbo rotary sport coupe",
        "model_silhouette": "low sculptural fastback coupe with long hood, contoured double-bubble roof, and integrated rear spoiler",
        "exterior_color_material": "deep metallic crimson-red paint with gloss black front lip and diffuser",
        "dimensions_proportions": "4.28 m length, 1.23 m low height, wide rear fenders",
        "wheels_axles": "4 wheels on 2 axles, 18-inch silver twin-spoke forged rims with wide rear tires",
        "lights_accessories": "sleek fixed fairing headlights, amber front turn lamps, A-pillar twin boost gauges inside cockpit",
        "interior_layout": "LEFT-HAND DRIVE: wrap-around driver cockpit on the left, deep bucket seats, rotary 9000-rpm tachometer centered in cluster",
        "steering_side": "LEFT",
        "default_driver": "MICDO",
        "default_passengers": [],
        "description": "Deep-red rotary sport coupe with sleek aerodynamic body, silver twin-spoke rims and cockpit boost gauges.",
        "damage_states": [
            ((1, 1), (40, 6), "spotless metallic crimson finish, crisp rotary idle and instant boost response"),
        ],
    },
    "CHARGER": {
        "vehicle_id": "CHARGER",
        "name": "the 1970 Matte-Black Supercharged Muscle Car",
        "vehicle_type": "classic 1970 American 2-door fastback muscle car",
        "model_silhouette": "long boxy muscular hood, wide recessed chrome-trimmed grille, coke-bottle side profile, towering roots supercharger scoop protruding through hood cutout",
        "exterior_color_material": "deep satin-black bodywork with mirror-chromed supercharger housing, triple-butterfly intake scoop, and chrome bumpers",
        "dimensions_proportions": "5.28 m length, 1.95 m width, heavy rear-biased drag stance",
        "wheels_axles": "4 wheels on 2 axles, 15-inch polished Cragar-style 5-spoke wheels with wide high-sidewall rear drag slicks",
        "lights_accessories": "concealed quad headlights behind wide front grille, dual side-exit exhaust pipes, mechanical blower belt spinning through hood opening",
        "interior_layout": "LEFT-HAND DRIVE: black vinyl high-back bucket seats, wood-rimmed 3-spoke steering wheel on the left, T-handle floor shifter, roll bar behind front seats",
        "steering_side": "LEFT",
        "default_driver": "MICDO",
        "default_passengers": [],
        "description": "Classic 1970 matte-black muscle car with a towering chrome supercharger blower rising through the hood.",
        "damage_states": [
            ((24, 1), (37, 2), "pristine garage-kept condition under canvas cover, polished chrome supercharger gleaming"),
            ((37, 3), (39, 4), "roaring at full 900-hp supercharged output, front tires lifting under launch torque"),
            ((39, 5), (39, 6), "dented front right fender and steaming radiator after a controlled stunt spin past the rail crossing"),
            ((40, 1), (40, 6), "resting upright on the dirt shoulder past the crossing with dented front fascia and white radiator steam rising gently into the dusk breeze"),
        ],
    },
    "SUPRA_SHELL": {
        "vehicle_id": "SUPRA_SHELL",
        "name": "the Rusted Orange Sport Coupe Project Shell",
        "vehicle_type": "2-door sport coupe rolling project chassis",
        "model_silhouette": "long-hood fastback coupe body with dented fenders and missing front grille inserts",
        "exterior_color_material": "oxidized faded-orange primer and bare sanded steel patches, intact twin-turbo inline-6 engine block under the hood",
        "dimensions_proportions": "4.51 m length, 1.81 m width",
        "wheels_axles": "4 mismatched steel transport wheels on 2 axles",
        "lights_accessories": "hazed headlamp housings, open hood revealing complete twin-turbo 2JZ-style block",
        "interior_layout": "LEFT-HAND DRIVE: stripped metal cabin with driver seat on the left",
        "steering_side": "LEFT",
        "default_driver": "TOM",
        "default_passengers": [],
        "description": "Rusted, dented orange sport coupe rolling shell on a flatbed tow truck before rebuild, carrying an intact twin-turbo engine block under the hood.",
        "damage_states": [
            ((22, 1), (22, 6), "dented weathered rolling shell on flatbed tow truck with intact twin-turbo engine block inside bay"),
        ],
    },
    "SUPRA": {
        "vehicle_id": "SUPRA",
        "name": "the Rebuilt 10-Second Metallic-Orange Twin-Turbo Coupe",
        "vehicle_type": "high-output 2-door twin-turbo targa sport coupe",
        "model_silhouette": "muscular rounded fastback coupe with wide rear arches, front intercooler mouth, and high hoop rear wing",
        "exterior_color_material": "lustrous pearl metallic-orange paint with silver twin-scroll turbo plumbing visible through the front bumper grille",
        "dimensions_proportions": "4.51 m length, 1.81 m width, 1.27 m height, balanced track stance",
        "wheels_axles": "4 wheels on 2 axles, 18-inch 5-spoke silver racing wheels with drilled brake rotors",
        "lights_accessories": "crystal multi-projector headlights, quad round taillights, removable targa roof panel",
        "interior_layout": "LEFT-HAND DRIVE: wraparound cockpit angled toward the left-hand driver seat, blue-stitched sport seats, dash boost controller",
        "steering_side": "LEFT",
        "default_driver": "TOM",
        "default_passengers": ["AMI"],
        "description": "Rebuilt 10-second bright metallic-orange twin-turbo sport coupe with removable targa roof and high rear wing.",
        "damage_states": [
            ((23, 1), (33, 6), "freshly painted metallic-orange finish, polished twin-turbo engine bay"),
            ((34, 1), (35, 6), "targa roof panel removed for high-speed highway rescue beside the semi-truck, light desert dust on lower rockers"),
            ((37, 1), (39, 6), "high-speed pursuit trim with minor right-side rub mark from contact with motorcycle, engine running clean"),
            ((40, 1), (40, 4), "parked on the desert shoulder beside the dented Charger with its twin-turbo engine ready for immediate launch"),
            ((40, 5), (40, 5), "driver door opened by Tom as Micdo climbs into the left-hand seat, fires the twin-turbo engine, and launches toward the dusk horizon"),
            ((40, 6), (40, 6), "speeding away into the distant amber dusk horizon with quad round taillights receding down the straight desert road"),
        ],
    },
    "JETTA": {
        "vehicle_id": "JETTA",
        "name": "the Alpine-White Tuned Sport Sedan",
        "vehicle_type": "4-door compact sport-tuned sedan",
        "model_silhouette": "clean angular 4-door notchback sedan with front chin spoiler and low rear deck wing",
        "exterior_color_material": "gloss alpine-white paint with clean monochrome bumpers",
        "dimensions_proportions": "4.39 m length, 1.73 m width, 1.44 m height",
        "wheels_axles": "4 wheels on 2 axles, 17-inch multi-spoke white powder-coated alloy wheels",
        "lights_accessories": "clear rectangular headlights, custom dash telemetry screen",
        "interior_layout": "LEFT-HAND DRIVE: white-trimmed sport seats, driver seat on the left, digital shift indicator",
        "steering_side": "LEFT",
        "default_driver": "SEJA",
        "default_passengers": [],
        "description": "Prized alpine-white tuned sport sedan with white alloy rims and custom dashboard telemetry display.",
        "damage_states": [
            ((28, 1), (36, 6), "clean alpine-white finish, desert dust along lower tires after Mojave drag run"),
        ],
    },
    "S2000": {
        "vehicle_id": "S2000",
        "name": "the Jet-Black Open Roadster",
        "vehicle_type": "2-door open-top high-revving sport roadster",
        "model_silhouette": "long hood, short rear deck, low windshield header, dual roll hoops behind seats",
        "exterior_color_material": "mirror-gloss jet-black paint with dark gunmetal aero lip",
        "dimensions_proportions": "4.13 m length, 1.75 m width, 1.28 m height",
        "wheels_axles": "4 wheels on 2 axles, 18-inch forged dark-chrome wheels",
        "lights_accessories": "sharp xenon projector headlights, concealed dual NOS plumbing beneath seats",
        "interior_layout": "LEFT-HAND DRIVE: red-and-black leather bucket seats, digital bar-graph tachometer on the left",
        "steering_side": "LEFT",
        "default_driver": "NYTRAN",
        "default_passengers": [],
        "description": "Jet-black open-top roadster with concealed dual Nitrous Oxide system under the driver seat.",
        "damage_states": [
            ((28, 1), (30, 6), "gleaming jet-black bodywork with concealed NOS purge valves active"),
        ],
    },
    "MOTO_PACK": {
        "vehicle_id": "MOTO_PACK",
        "name": "the Matte-Black Street Sport Motorcycles",
        "vehicle_type": "high-displacement full-fairing street sport motorcycles",
        "model_silhouette": "aggressive aerodynamic front fairing, clip-on handlebars, high tail section",
        "exterior_color_material": "matte-black carbon-textured fairings with dark smoked windscreens",
        "dimensions_proportions": "2.05 m length, 1.12 m height",
        "wheels_axles": "2 wheels on 2 axles per motorcycle, 17-inch black cast alloy wheels",
        "lights_accessories": "twin narrow LED headlights, high-mount exhaust canisters",
        "interior_layout": "CENTER RIDER ASTRIDE: clip-on handlebars with right-hand throttle grip and front brake lever",
        "steering_side": "CENTER",
        "default_driver": "NYTRAN",
        "default_passengers": ["CELA"],
        "description": "Matte-black high-displacement street sport motorcycles with carbon-textured fairings.",
        "damage_states": [
            ((18, 1), (20, 6), "pack of matte-black sport motorcycles circling in tight formation"),
            ((36, 1), (37, 6), "two matte-black sport motorcycles ridden in high-speed pursuit formation"),
            ((38, 1), (38, 6), "lead motorcycle loses balance after side-contact on the hill road and slides down the concrete channel embankment"),
        ],
    },
    "F150_TRUCK": {
        "vehicle_id": "F150_TRUCK",
        "name": "the Bright-Red Stepside Shop Pickup Truck",
        "vehicle_type": "2-door flareside shop pickup truck",
        "model_silhouette": "classic stepside pickup cab with open rear cargo bed carrying wooden parts crates",
        "exterior_color_material": "bright shop-red paint with chrome front bumper",
        "dimensions_proportions": "5.3 m length, 1.85 m height",
        "wheels_axles": "4 wheels on 2 axles, 16-inch alloy wheels",
        "lights_accessories": "rectangular halogen headlights, chrome side mirrors",
        "interior_layout": "LEFT-HAND DRIVE: bench seat with driver position on the left",
        "steering_side": "LEFT",
        "default_driver": "TOM",
        "default_passengers": [],
        "description": "Bright-red shop pickup truck carrying wooden auto-parts crates in the rear bed.",
        "damage_states": [
            ((5, 1), (10, 6), "clean shop-red pickup parked at Toto kerb or Ver's Geh bay"),
        ],
    },
}

OBJECT_LOCK: dict[str, dict[str, Any]] = {
    "HARPOON_CABLE": {
        "object_id": "HARPOON_CABLE",
        "name": "Pneumatic Steel Tether Launcher & Tension Cable",
        "category": "tactical_rigging",
        "material_appearance": "compact matte-black pneumatic tube rig extending a 3-prong magnetic steel tether clamp attached to a braided 10 mm steel winch cable",
        "default_owner": "CEVIN",
        "description": "Heavy-duty pneumatic steel-cable tether rig and high-tensile safety tether line linking the coupe and truck cabin.",
        "state_by_scene": [
            ((2, 1), (4, 6), "anchored taut between lead black Civic sunroof and semi-truck right cab pillar, then detached cleanly"),
            ((32, 1), (33, 6), "clamped to semi-truck cab frame with braided steel cable taut beside the moving trailer"),
            ((34, 1), (34, 6), "severed cleanly by Tom's heavy steel cutters to free Cevin onto the Supra hood"),
        ],
    },
    "BREACH_CHARGE": {
        "object_id": "BREACH_CHARGE",
        "name": "Magnetic Container Latch Release Module",
        "category": "electronic_tool",
        "material_appearance": "palm-sized matte-grey magnetic actuator clamp with amber status LED",
        "default_owner": "CINA",
        "description": "Compact magnetic remote latch-release module attached to the rear container door lock.",
        "state_by_scene": [
            ((3, 1), (3, 6), "clamped onto the rear container lock bar, amber LED pulsing before releasing the steel latch"),
        ],
    },
    "TUNA_SANDWICH": {
        "object_id": "TUNA_SANDWICH",
        "name": "Crustless Tuna Sandwich & Iced Water",
        "category": "diner_prop",
        "material_appearance": "white ceramic diner plate holding two halves of a crustless white-bread tuna salad sandwich beside a tall glass of iced water",
        "default_owner": "AMI",
        "description": "White ceramic plate holding a crustless tuna sandwich and a tall glass of iced water on the Toto counter.",
        "state_by_scene": [
            ((6, 1), (7, 6), "freshly plated on the wooden lunch counter between Ami and Tom"),
        ],
    },
    "PINK_SLIP": {
        "object_id": "PINK_SLIP",
        "name": "Vehicle Title Registration Certificate",
        "category": "document",
        "material_appearance": "folded official paper vehicle title certificate inside a clear plastic sleeve, no readable text",
        "default_owner": "TOM",
        "description": "Official vehicle title registration certificate folded inside a clear protective sleeve.",
        "state_by_scene": [
            ((11, 1), (13, 6), "held in Tom's right hand and placed on the hood for the quarter-mile wager"),
            ((28, 1), (29, 6), "Seja's white Jetta title sleeve handed to the Race Wars starter"),
        ],
    },
    "NOS_BOTTLES": {
        "object_id": "NOS_BOTTLES",
        "name": "Twin High-Pressure Nitrous Oxide Cylinders",
        "category": "vehicle_component",
        "material_appearance": "two anodized cobalt-blue aluminum pressure cylinders with braided stainless lines and a red steering-wheel thumb switch",
        "default_owner": "TOM",
        "description": "Twin blue high-pressure Nitrous Oxide cylinders mounted behind the cockpit with a red steering-wheel trigger button.",
        "state_by_scene": [
            ((10, 1), (15, 6), "mounted in the rear frame of Tom's neon-green Eclipse, stage-1 and stage-2 valves engaged during the drag race"),
            ((19, 1), (19, 6), "venting pressure in the rear of the disabled Eclipse alongside theatrical orange smoke"),
        ],
    },
    "DIAG_LAPTOP": {
        "object_id": "DIAG_LAPTOP",
        "name": "Ruggedized ECU Telemetry Laptop",
        "category": "electronic_tool",
        "material_appearance": "brushed-silver rugged laptop connected via coiled OBD cable, screen showing graphical boost curves without readable text",
        "default_owner": "SEJA",
        "description": "Ruggedized silver tuning laptop displaying engine manifold pressure curves and overload warnings without readable text.",
        "state_by_scene": [
            ((11, 1), (29, 6), "open on passenger dash or pit table showing colored telemetry curves without readable text"),
        ],
    },
    "CASE_FILES": {
        "object_id": "CASE_FILES",
        "name": "LAPD-FBI Highway Investigation Folders",
        "category": "document",
        "material_appearance": "thick manila case folders, pinned highway route maps, and glossy surveillance photographs without readable text",
        "default_owner": "NESE",
        "description": "Thick manila highway-heist investigation folders, satellite route maps and customs manifests without readable text.",
        "state_by_scene": [
            ((9, 1), (9, 6), "spread across the oak tactical table inside the task-force villa"),
        ],
    },
    "WRENCH_KIT": {
        "object_id": "WRENCH_KIT",
        "name": "Chrome Torque Wrench & Garage Tool Set",
        "category": "mechanic_tool",
        "material_appearance": "heavy chrome ratchet torque wrench, steel socket tray, and chain engine hoist",
        "default_owner": "ONLE",
        "description": "Heavy chrome torque wrench, socket tray and engine hoist chains inside the garage.",
        "state_by_scene": [
            ((5, 1), (24, 6), "used on the workbench and engine bay inside the tuning garage"),
        ],
    },
    "POLICE_RADIO": {
        "object_id": "POLICE_RADIO",
        "name": "Encrypted LAPD Tactical Radio Handset",
        "category": "communication_device",
        "material_appearance": "matte-black heavy-duty encrypted tactical transceiver with stub antenna and coiled speaker mic",
        "default_owner": "TOM",
        "description": "Tom's concealed LAPD encrypted tactical radio handset used for emergency medevac coordination.",
        "state_by_scene": [
            ((35, 1), (35, 6), "gripped in Tom's right hand on the desert highway shoulder to call emergency medevac helicopter"),
        ],
    },
    "SUPRA_KEY": {
        "object_id": "SUPRA_KEY",
        "name": "Metallic-Orange Supra Ignition Key",
        "category": "key_prop",
        "material_appearance": "single black-headed metal ignition key on a brushed steel split ring",
        "default_owner": "TOM",
        "description": "Single metal ignition key to the orange 10-second sport coupe on a steel ring.",
        "state_by_scene": [
            ((40, 1), (40, 2), "tucked inside Tom's leather jacket pocket while he helps Micdo clear of the steaming Charger"),
            ((40, 3), (40, 3), "reached for inside Tom's leather jacket pocket by his right hand beside the orange Supra"),
            ((40, 4), (40, 4), "held steady in Tom's open right palm on its brushed steel ring between Tom and Micdo"),
            ((40, 5), (40, 5), "pressed firmly by Tom into Micdo's hand and inserted into the orange Supra ignition"),
            ((40, 6), (40, 6), "engaged inside the orange Supra ignition as Micdo drives into the distant dusk horizon"),
        ],
    },
    "CUSTOMS_INVOICE": {
        "object_id": "CUSTOMS_INVOICE",
        "name": "Stamped Customs Clearance Ledger",
        "category": "document",
        "material_appearance": "hardbound shipping ledger with red customs seal impressions, no readable text",
        "default_owner": "NESE",
        "description": "Stamped customs clearance ledger and legal import manifests inside Ny Tran's bonded warehouse.",
        "state_by_scene": [
            ((27, 1), (27, 6), "opened on the warehouse inspection desk showing official red customs seals"),
        ],
    },
}

ENVIRONMENT_LOCK: dict[str, dict[str, Any]] = {
    "HIGHWAY_NIGHT": {
        "location_id": "HIGHWAY_NIGHT",
        "category": "highway",
        "architecture_layout": "four-lane divided interstate highway cutting straight across dark desert hills, concrete center jersey barrier",
        "road_lane_geometry": "four wide eastbound asphalt lanes (right-hand US traffic), dashed white lane dividers, amber reflector studs, wide paved right shoulder",
        "terrain_landmarks": "low silhouetted Mojave foothills against a moonlit night sky, no readable highway signs",
        "interior_furniture_objects": "none (open highway corridor)",
        "weather_atmosphere": "clear dry night air, high-speed slipstream wind, subtle tire haze",
        "orientation_axis": "vehicles travel consistently screen-left to screen-right along the eastbound lanes; camera stays on the south (right-flank) 180-degree axis",
        "ambient_sound": "deep diesel rig rumble, high-rpm tuned exhausts and highway wind",
        "description": "Interstate 10 highway at night: four wide asphalt lanes cutting through dark desert hills, amber reflector studs along the divider, long headlight beams slicing the dark, no readable road signs.",
    },
    "RIG_CABIN": {
        "location_id": "RIG_CABIN",
        "category": "vehicle_interior",
        "architecture_layout": "elevated 18-wheel semi-truck cab interior, wide two-piece windshield, left driver door and right passenger door",
        "road_lane_geometry": "highway lanes rushing beneath the cab hood visible through the windshield",
        "terrain_landmarks": "green underglow reflections in the wide side mirrors",
        "interior_furniture_objects": "high leather air-ride driver seat on the LEFT, 18-inch steering wheel, amber analog gauges, floor gear lever at center, passenger seat on the RIGHT",
        "weather_atmosphere": "amber dashboard glow inside cab, rushing night wind through open right window",
        "orientation_axis": "camera looks across the cab from the right passenger side toward the left driver seat, preserving forward motion left-to-right",
        "ambient_sound": "diesel cabin vibration, air-horn valve and wind rushing past glass",
        "description": "Interior of the 18-wheel semi-truck cab at night: high leather driver seat on the left, large steering wheel, amber dashboard gauges, wide side mirrors reflecting green underglow behind, passenger window on the right.",
    },
    "VERS_GARAGE": {
        "location_id": "VERS_GARAGE",
        "category": "indoor_workshop",
        "architecture_layout": "high-bay Los Angeles performance tuning shop with corrugated steel roof, two-post hydraulic car lifts, and wide roll-up street bay door",
        "road_lane_geometry": "concrete shop floor leading out to sunlit urban kerb",
        "terrain_landmarks": "sunlit Los Angeles palm silhouettes visible outside the open bay door",
        "interior_furniture_objects": "red steel tool chests, workbenches, racks of polished aluminum intakes and turbochargers, hydraulic lift arms",
        "weather_atmosphere": "warm morning sunbeams slicing through dusty garage air",
        "orientation_axis": "open bay door at screen right, hydraulic lift at center, workbench at screen left",
        "ambient_sound": "air wrench whir, metal tools clinking and distant city traffic",
        "description": "The Ver's Geh auto parts and tuning shop in Los Angeles: high corrugated roof, hydraulic car lifts, tool chests, racks of chrome intakes and turbochargers, sunny roll-up bay door opening to the street, no readable brand logos.",
    },
    "TOTO_DINER": {
        "location_id": "TOTO_DINER",
        "category": "indoor_diner",
        "architecture_layout": "corner neighborhood grocery and sandwich counter with sunlit front plate-glass windows",
        "road_lane_geometry": "street kerb visible through the front window behind the counter stools",
        "terrain_landmarks": "Echo Park street trees outside the front glass",
        "interior_furniture_objects": "long polished wooden lunch counter running left-to-right, fixed chrome stools with red vinyl seats, glass display shelves, kitchen pass-through behind Ami",
        "weather_atmosphere": "warm midday California sunlight streaming through front windows, lazy ceiling fan rotation",
        "orientation_axis": "Ami stands behind the counter on screen left facing right; Tom sits on a chrome stool on screen right facing left",
        "ambient_sound": "ceiling fan hum, plates clinking and midday street traffic outside",
        "description": "Toto family grocery and sandwich counter at midday: sunlit front windows, long wooden lunch counter with chrome stools, glass display shelves, kitchen pass-through behind the counter, no readable signs.",
    },
    "TOTO_PATIO": {
        "location_id": "TOTO_PATIO",
        "category": "outdoor_urban",
        "architecture_layout": "sunlit concrete sidewalk patio outside Toto grocery shaded by a striped canvas awning",
        "road_lane_geometry": "two-lane residential Los Angeles street with kerbside parking along the right",
        "terrain_landmarks": "palm-lined Echo Park hillside in the background",
        "interior_furniture_objects": "wooden picnic tables on the concrete patio, low steps leading to the diner entrance",
        "weather_atmosphere": "crisp midday sunshine, clear shadows on concrete",
        "orientation_axis": "diner entrance on screen left, kerbside parked cars on screen right",
        "ambient_sound": "street breeze, shoes scuffling on concrete and idling engines",
        "description": "Sunlit concrete patio outside Toto grocery: wooden lunch tables under a canvas awning, kerbside parking along the palm-lined Los Angeles street, red pickup and lowered street cars parked at the kerb.",
    },
    "TASKFORCE_HQ": {
        "location_id": "TASKFORCE_HQ",
        "category": "indoor_command",
        "architecture_layout": "hillside Spanish-revival villa room repurposed as an LAPD-FBI covert briefing room with tall arched windows and wooden shutters",
        "road_lane_geometry": "interior tiled floor",
        "terrain_landmarks": "slatted daylight filtering from the hillside terrace",
        "interior_furniture_objects": "large oak tactical table at center, cork pinboards with highway route maps and vehicle surveillance photos, steel file cabinets",
        "weather_atmosphere": "cool indoor shade cut by warm afternoon window slats",
        "orientation_axis": "Nese and Kinan on screen left of the tactical table facing right; Tom on screen right facing left",
        "ambient_sound": "air-conditioner hum, footsteps on tile and rustling case folders",
        "description": "Abandoned hillside Spanish-style villa converted into a covert LAPD-FBI task-force operations room: tall arched windows with slatted blinds, tactical tables, highway route maps and pinboards with vehicle photos, no readable text.",
    },
    "RACE_MEET": {
        "location_id": "RACE_MEET",
        "category": "outdoor_urban",
        "architecture_layout": "wide industrial avenue between tall concrete freight warehouses in South Los Angeles at night",
        "road_lane_geometry": "straight four-lane industrial asphalt avenue converted into a 1/4-mile street drag strip with painted white starting line",
        "terrain_landmarks": "sodium streetlamps, rows of parked tuned coupes lining both kerbs",
        "interior_furniture_objects": "portable sound-system trunk setups, oil-drum barriers along the starting line",
        "weather_atmosphere": "warm orange sodium floodlights, drifting white tire smoke, neon underglow reflections on asphalt",
        "orientation_axis": "race cars line up facing screen-left to screen-right toward the down-avenue finish line",
        "ambient_sound": "thumping bass, revving tuned engines and cheering street crowd",
        "description": "South Los Angeles industrial warehouse district at night: wide asphalt avenue between concrete warehouses, hundreds of colorful tuned street cars parked under sodium floodlights, tire smoke drifting, no readable banners.",
    },
    "RACE_COCKPIT": {
        "location_id": "RACE_COCKPIT",
        "category": "vehicle_interior",
        "architecture_layout": "tight street-race coupe cockpit at night during full-throttle acceleration",
        "road_lane_geometry": "industrial drag avenue streaking past the windshield and side windows",
        "terrain_landmarks": "sodium warehouse lamps blurring into horizontal amber streaks outside",
        "interior_furniture_objects": "left-hand bucket seat, leather sport wheel with red thumb NOS button, glowing tachometer and boost gauge, passenger-side telemetry laptop",
        "weather_atmosphere": "blue-and-amber gauge light across driver's face, vibration at 180 km/h",
        "orientation_axis": "camera mounted inside cabin on the right looking left at the driver and forward through the windshield",
        "ambient_sound": "screaming twin-cam engine, turbocharger whistle and gear shifts",
        "description": "Interior cockpit of the tuned street race coupe at night: bucket seats, leather steering wheel with red NOS thumb button, glowing dashboard tachometers, passenger-side telemetry laptop screen, sodium streetlights streaking past the windshield.",
    },
    "RACE_ALLEY": {
        "location_id": "RACE_ALLEY",
        "category": "outdoor_urban",
        "architecture_layout": "narrow brick-walled industrial service alley behind South L.A. warehouses at night",
        "road_lane_geometry": "single-lane wet asphalt service road flanked by loading docks",
        "terrain_landmarks": "red-and-blue patrol car light bars flashing at the distant street mouth",
        "interior_furniture_objects": "stacked wooden pallets, chain-link gates, steel dumpsters",
        "weather_atmosphere": "wet asphalt reflecting pulsing red-and-blue patrol strobes and amber warehouse lamps",
        "orientation_axis": "escape route runs screen-left to screen-right toward the dark side street",
        "ambient_sound": "distant police sirens, echoing footsteps and skidding tires",
        "description": "Narrow industrial back alley behind the South L.A. warehouses at night: brick walls, stacked wooden pallets, chain-link fences, red-and-blue patrol lights reflecting off wet asphalt at both ends.",
    },
    "SAIGON_LOT": {
        "location_id": "SAIGON_LOT",
        "category": "outdoor_urban",
        "architecture_layout": "fenced gravel storage lot on the edge of Little Saigon at night bordered by stacked rusted shipping containers",
        "road_lane_geometry": "compacted gravel yard with a single chain-link gate entrance",
        "terrain_landmarks": "distant blurred neon shop glow beyond the perimeter fence",
        "interior_furniture_objects": "rusted steel containers, ring of matte-black sport motorcycles parked with headlights aimed inward",
        "weather_atmosphere": "hard motorcycle headlight beams cutting through night dust and smoke",
        "orientation_axis": "Tom and Micdo beside the neon-green Eclipse on screen left; Ny Tran and Cela with their motorcycle pack on screen right",
        "ambient_sound": "idling sport-bike engines, gravel crunching and night wind",
        "description": "Desolate gravel lot at the edge of Little Saigon at night: rusted shipping containers, chain-link perimeter fence, neon shop glow far behind, circle of matte-black sport motorcycles surrounding the parked coupe.",
    },
    "TOTO_BACKYARD": {
        "location_id": "TOTO_BACKYARD",
        "category": "outdoor_urban",
        "architecture_layout": "warm residential backyard behind the Toto family clapboard house in Echo Park at evening",
        "road_lane_geometry": "concrete side driveway leading back to the detached two-bay garage",
        "terrain_landmarks": "wooden perimeter fence, overhead strings of warm tungsten patio bulbs",
        "interior_furniture_objects": "long wooden family dining table, cast-iron charcoal barbecue grill, folding lawn chairs",
        "weather_atmosphere": "warm amber string-light glow, drifting barbecue smoke under a deep evening sky",
        "orientation_axis": "dining table centered; house porch on screen left, garage driveway on screen right",
        "ambient_sound": "charcoal grill sizzle, clinking bottles and warm evening crickets",
        "description": "Backyard of the Toto family house in Echo Park at dusk and night: string lights over a long wooden dining table, smoking charcoal barbecue grill, lawn edged with wooden fencing, open driveway leading to the home garage.",
    },
    "TOTO_GARAGE": {
        "location_id": "TOTO_GARAGE",
        "category": "indoor_workshop",
        "architecture_layout": "detached two-bay timber-and-concrete home garage behind the Toto house",
        "road_lane_geometry": "oil-darkened concrete floor opening onto the backyard driveway",
        "terrain_landmarks": "rear alcove housing the covered 1970 matte-black Charger",
        "interior_furniture_objects": "overhead chain engine hoist, steel workbenches with manifolds and torque wrenches, hanging shop lamps",
        "weather_atmosphere": "warm tungsten overhead work lamps, realistic shadows on concrete and polished metal",
        "orientation_axis": "project car bay at center-left; 1970 Charger bay at center-right",
        "ambient_sound": "ratchet wrenches turning, chain hoist clinking and fluorescent hum",
        "description": "Detached two-bay garage behind the Toto house: warm overhead work lamps, engine hoist, workbenches stacked with wrenches and manifolds, concrete floor, rear corner holding the covered 1970 muscle car.",
    },
    "NYTRAN_MANSION": {
        "location_id": "NYTRAN_MANSION",
        "category": "outdoor_urban",
        "architecture_layout": "walled Little Saigon courtyard residence with wrought-iron front gates and stone driveway",
        "road_lane_geometry": "wide cobbled circular driveway in front of the main veranda",
        "terrain_landmarks": "tall cypress hedges and modern concrete portico",
        "interior_furniture_objects": "black unmarked command SUV parked near the gate, stone veranda columns",
        "weather_atmosphere": "cool blue-gold dawn light with long early-morning shadows",
        "orientation_axis": "command SUV on screen left; mansion veranda and courtyard on screen right",
        "ambient_sound": "tactical boots on stone, helicopter blades high overhead and rustling papers",
        "description": "Courtyard and living hall of Ny Tran's gated Little Saigon residence at dawn: wrought-iron front gates, stone driveway, modern living room with leather sofas and silk wall panels.",
    },
    "NYTRAN_WAREHOUSE": {
        "location_id": "NYTRAN_WAREHOUSE",
        "category": "indoor_workshop",
        "architecture_layout": "high-ceiling customs-bonded electronics storage warehouse behind Ny Tran's compound",
        "road_lane_geometry": "wide concrete forklift aisle between steel pallet racks",
        "terrain_landmarks": "high clerestory skylights letting in morning sunbeams",
        "interior_furniture_objects": "tall steel shelving stacked with sealed brown cartons, steel inspection desk holding stamped customs ledgers",
        "weather_atmosphere": "clean morning skylight beams cutting through cool warehouse shade",
        "orientation_axis": "inspection desk on screen left; pallet racks receding to screen right",
        "ambient_sound": "echoing footsteps on concrete and flipping ledger pages",
        "description": "Large customs-bonded electronics warehouse behind Ny Tran's compound: tall steel shelving stacked with sealed brown cartons, forklift aisle, inspection desk with stamped shipping ledgers, high skylight windows.",
    },
    "RACE_WARS": {
        "location_id": "RACE_WARS",
        "category": "desert_airfield",
        "architecture_layout": "Mojave Desert airfield drag strip and paddock under midday sun",
        "road_lane_geometry": "two-lane concrete runway drag strip with Christmas-tree starting lights, bordered by pit canopies",
        "terrain_landmarks": "arid Mojave mountain range shimmering across the horizon",
        "interior_furniture_objects": "shade canopies, folding tool tables, timing light tree at the starting line",
        "weather_atmosphere": "blazing desert sunlight, visible heat haze rising off concrete tarmac",
        "orientation_axis": "drag strip runs screen-left to screen-right toward the desert mountain horizon",
        "ambient_sound": "roaring engines, desert wind and crowd murmur across the tarmac",
        "description": "Mojave Desert Race Wars airfield under blazing midday sun: vast heat-shimmering concrete runway, canopies and pit tents lined with tuned cars, desert mountains on the horizon, two-lane drag strip with starting lights.",
    },
    "DESERT_HIGHWAY": {
        "location_id": "DESERT_HIGHWAY",
        "category": "highway",
        "architecture_layout": "long straight two-lane asphalt highway cutting across open Mojave scrubland in late afternoon",
        "road_lane_geometry": "two wide asphalt lanes with yellow center dashed line and wide compacted sand shoulders on both sides",
        "terrain_landmarks": "dry desert brush, distant rocky buttes, telegraph poles rushing past",
        "interior_furniture_objects": "none (open desert highway)",
        "weather_atmosphere": "golden late-afternoon sun, swirling sand dust along the road shoulders, heat shimmer",
        "orientation_axis": "semi-truck and pursuit cars travel screen-left to screen-right; camera holds the south roadside axis",
        "ambient_sound": "heavy diesel engine, high-speed wind and tires roaring on hot asphalt",
        "description": "Two-lane desert highway cutting across arid scrubland under late-afternoon sun: long straight asphalt, sandy shoulders, heat haze rising in the distance, no readable highway signs.",
    },
    "TOTO_FRONT": {
        "location_id": "TOTO_FRONT",
        "category": "outdoor_urban",
        "architecture_layout": "tree-lined residential street in front of the Toto family two-story white clapboard house at sunset",
        "road_lane_geometry": "two-lane residential asphalt street along the front kerb and concrete driveway",
        "terrain_landmarks": "wooden front porch steps, green front lawn, palm trees catching golden-hour sun",
        "interior_furniture_objects": "porch railing, driveway gate leading back to the garage",
        "weather_atmosphere": "warm amber golden-hour sunset casting long shadows across the lawn and asphalt",
        "orientation_axis": "Toto porch and lawn on screen left; residential street on screen right",
        "ambient_sound": "evening breeze through palm fronds and approaching engines",
        "description": "Tree-lined residential street in front of the Toto family white clapboard house at golden-hour sunset: front lawn, concrete porch steps, driveway leading back to the garage.",
    },
    "LA_HILLS_ROAD": {
        "location_id": "LA_HILLS_ROAD",
        "category": "hillside_road",
        "architecture_layout": "steep descending asphalt boulevard in the Los Angeles hills overlooking a concrete storm-drain channel",
        "road_lane_geometry": "two wide downhill lanes bordered by concrete retaining walls and a lower embankment along the concrete flood channel",
        "terrain_landmarks": "palm trees, city basin skyline glowing in sunset haze below",
        "interior_furniture_objects": "concrete guard blocks along the channel rim",
        "weather_atmosphere": "dramatic orange sunset raking across the sloped asphalt and concrete walls",
        "orientation_axis": "pursuit moves downhill screen-left to screen-right",
        "ambient_sound": "supercharger whine, screaming tires and roaring exhausts",
        "description": "Steep, sloping asphalt avenues in the Los Angeles hills at sunset: palm trees, concrete retaining walls, long downhill intersections overlooking the city basin, concrete storm-drain channel below the lower curve.",
    },
    "RAIL_CROSSING": {
        "location_id": "RAIL_CROSSING",
        "category": "rail_crossing",
        "architecture_layout": "industrial outskirts two-lane road intersecting an active steel freight railroad line at sunset",
        "road_lane_geometry": "straight two-lane asphalt road rising slightly over timber-and-steel railroad tracks",
        "terrain_landmarks": "flashing red railroad signal masts, striped crossing gate arms, steel freight locomotive approaching from the right",
        "interior_furniture_objects": "railroad signal crossbuck post (without readable text), wooden gate arm",
        "weather_atmosphere": "deep amber sunset sky, flashing red signal reflections on the two hoods",
        "orientation_axis": "Charger in left lane and Supra in right lane race forward screen-left to screen-right across the tracks",
        "ambient_sound": "clanging railroad crossing bell, freight train horn and rumbling V8 engine",
        "description": "Outskirts industrial railroad crossing at sunset: two-lane road rising over steel train tracks, red flashing crossing signals, lowering striped wooden gate arms, steel freight train approaching on the right track, open desert road beyond.",
    },
    "CROSSING_BEYOND": {
        "location_id": "CROSSING_BEYOND",
        "category": "highway",
        "architecture_layout": "open desert road and wide dirt shoulder immediately beyond the railroad crossing at dusk",
        "road_lane_geometry": "two-lane desert asphalt stretching straight toward the dusk horizon with a wide gravel shoulder",
        "terrain_landmarks": "railroad embankment behind, open desert horizon ahead",
        "interior_furniture_objects": "dented 1970 matte-black Charger resting upright on the dirt shoulder, metallic-orange Supra parked beside it",
        "weather_atmosphere": "cobalt-and-amber dusk light, wisps of radiator steam rising in the cool desert breeze",
        "orientation_axis": "dented Charger on screen left, orange Supra at center-right pointing toward the open horizon on screen right",
        "ambient_sound": "ticking hot metal, distant approaching sirens and desert wind",
        "description": "Open desert road just past the railroad crossing at dusk: wide dirt shoulder, steaming muscle car resting upright on the shoulder, orange sport coupe stopped nearby, long straight road stretching toward the glowing horizon.",
    },
}

ACTION_STUNT_CHOREOGRAPHY_RULE: str = (
    "Action & martial arts stunt choreography rule: Professional stunt performers execute a tightly choreographed "
    "martial arts and action confrontation with unbroken kinematic flow from 0.0s to 10.0s. Fast defensive movements, "
    "precise dodges, controlled kicks, dramatic camera tracking, dynamic footwork and realistic physical reactions blend "
    "seamlessly across beats without mid-shot pauses. When a performer loses balance, they fall safely onto padded flooring "
    "outside the camera's view. Intense action-film atmosphere, realistic lighting, fluid handheld or gimbal cinematography, "
    "authentic Vietnamese action cinema. No blood, no graphic injuries, no gore. All movements are simulated stunt choreography."
)

PHYSICS_RULES: dict[str, str] = {
    "vehicle": (
        "Vehicle physics & fluid kinematics: vehicles obey real mass, progressive suspension compression, tire-asphalt grip, "
        "smooth steering geometry, and continuous forward momentum across 0.0s–10.0s; all wheels rotate in sync with ground speed "
        "and stay planted on the road surface; 18-wheel tractor and trailer articulate naturally at the fifth-wheel pivot; "
        "vehicle body dimensions, wheel count, paint color, and left-hand driver seat position never morph."
    ),
    "character": (
        "Human physics, fluid body follow-through & face lock: continuous natural weight transfer across the feet and hips, "
        "uninterrupted upper-body and hand follow-through while speaking (never freeze physical movement to deliver dialogue), "
        "natural balance and breathing through 10.0s; every visible named face stays faithful to its approved reference throughout "
        "the shot (eye shape, nose bridge, jawline, hair, and scars stable while turning); natural blinks and matched eyelines, no fixed stare."
    ),
    "hand_object": (
        "Hand & object mechanics: to pick up or handle an object a character reaches with a smooth arm arc, closes five natural fingers "
        "around its real weight, and carries its momentum cleanly in the established hand; objects never float, teleport, duplicate, or "
        "pass through hands; in a hand-over both hands stay visible until the receiver's fingers close; feet never slide on the ground."
    ),
    "environment": (
        "Environmental physics: shadows, reflections, wind slipstream, tire smoke, dust plumes, and heat shimmer respond smoothly and "
        "physically to vehicle speed and light direction through the final frame at 10.0s."
    ),
    "action_stunt": ACTION_STUNT_CHOREOGRAPHY_RULE,
}

CINEMATIC_STYLE: dict[str, Any] = {
    "aspect_ratio": "16:9",
    "frame_rate": 24,
    "clip_seconds": 10,
    "visual_style": (
        "Cinematic Vietnamese martial arts and street-racing action sequence, 10 seconds, photorealistic live-action, full-frame 16:9, 24fps, "
        "natural skin texture, subtle film grain, deep asphalt shadows, crisp neon and sodium highlights, authentic Vietnamese action cinema. "
        "No blood, no graphic injuries, no gore. All movements are simulated stunt choreography."
    ),
    "clean_frame": (
        "Clean cinematic frame, never TV footage: no TV channel or broadcaster logo, watermark, news ticker, lower-third, "
        "LIVE/REC badge, timestamp, or readable text on signs, pages, or screens."
    ),
}

AUDIO_STYLE: dict[str, Any] = {
    "language": "Vietnamese",
    "accent": "natural Southern Vietnamese accent",
    "narrator": {
        "name_vi": "Người dẫn chuyện",
        "voice": (
            "Narrator: an outside storyteller who is NOT a character in the film: one consistent mature Southern Vietnamese "
            "woman's voice, calm, low and warm, speaking about the person in the third person, used only to introduce a lead "
            "at first appearance. Every mouth in frame stays closed while she speaks; never lip-sync her words to anyone on screen."
        ),
        "voice_vi": (
            "Nữ khoảng năm mươi tuổi, giọng Nam Bộ (Sài Gòn); tông trầm ấm (alto), hơi khàn nhẹ; giọng kể điềm tĩnh, sâu lắng "
            "như người dẫn phim điện ảnh, nhịp chậm đều, khoảng ba rưỡi âm tiết mỗi giây. Không phải nhân vật trong cảnh: "
            "mọi miệng trên hình khép, không ai nhép theo lời bà."
        ),
    },
}

OMNI_MODEL_CAPABILITIES: dict[str, dict[str, Any]] = {
    "ingredients": {
        "workflow": "ingredients_r2v",
        "endpoint": "/api/flow/generate-video-omni",
        "max_references": 7,
        "requires_start_frame": False,
        "supports_character_tags": True,
        "duration_s": 10,
        "aspect_ratio": "16:9",
        "description": "Reference-guided Omni video generation using approved character/asset portraits for new scene cuts.",
    },
    "frames": {
        "workflow": "frame_i2v",
        "endpoint": "/api/flow/generate-video",
        "max_references": 1,
        "requires_start_frame": True,
        "supports_character_tags": False,
        "duration_s": 10,
        "aspect_ratio": "16:9",
        "description": "Exact-frame continuation from the extracted final frame of the preceding clip (`CONTINUE`).",
    },
    "text": {
        "workflow": "text_to_video",
        "endpoint": "/api/flow/generate-video-omni-text",
        "max_references": 0,
        "requires_start_frame": False,
        "supports_character_tags": False,
        "duration_s": 10,
        "aspect_ratio": "16:9",
        "description": "Pure text-to-video generation for establishing, environment, or vehicle/object insert shots without named leads.",
    },
    "insert": {
        "workflow": "insert_shot",
        "endpoint": "/api/flow/generate-video-omni-text",
        "max_references": 2,
        "requires_start_frame": False,
        "supports_character_tags": False,
        "duration_s": 10,
        "aspect_ratio": "16:9",
        "description": "Standalone mechanical/object/vehicle detail insert or B-roll take preserving scene time, lighting, and object state.",
    },
    "extend": {
        "workflow": "video_extend",
        "endpoint": "/api/flow/extend-video",
        "max_references": 0,
        "requires_start_frame": False,
        "supports_character_tags": False,
        "duration_s": 10,
        "aspect_ratio": "16:9",
        "description": "Native timeline extension of an existing generated clip up to 40s total.",
    },
    "edit": {
        "workflow": "video_edit",
        "endpoint": "/api/flow/edit-video",
        "max_references": 1,
        "requires_start_frame": False,
        "supports_character_tags": False,
        "duration_s": 10,
        "aspect_ratio": "16:9",
        "description": "In-place modification of an existing rendered video clip.",
    },
}

GLOBAL_FILM_BIBLE: dict[str, Any] = {
    "CHARACTER_LOCK": CHARACTER_LOCK,
    "VEHICLE_LOCK": VEHICLE_LOCK,
    "ENVIRONMENT_LOCK": ENVIRONMENT_LOCK,
    "OBJECT_LOCK": OBJECT_LOCK,
    "PHYSICS_RULES": PHYSICS_RULES,
    "CINEMATIC_STYLE": CINEMATIC_STYLE,
    "AUDIO_STYLE": AUDIO_STYLE,
    "OMNI_MODEL_CAPABILITIES": OMNI_MODEL_CAPABILITIES,
}


def resolve_vehicle_condition(vehicle_id: str, scene_num: int, clip_num: int) -> str:
    v = VEHICLE_LOCK.get(vehicle_id)
    if not v:
        return ""
    pos = (scene_num, clip_num)
    for start_pos, end_pos, cond in v.get("damage_states", []):
        if start_pos <= pos <= end_pos:
            return cond
    return "intact operational condition"


def resolve_object_condition(object_id: str, scene_num: int, clip_num: int) -> str:
    obj = OBJECT_LOCK.get(object_id)
    if not obj:
        return ""
    pos = (scene_num, clip_num)
    for start_pos, end_pos, cond in obj.get("state_by_scene", []):
        if start_pos <= pos <= end_pos:
            return cond
    return "intact established state"


def format_vehicle_lock_line(vehicle_id: str, scene_num: int, clip_num: int, state_override: str = "") -> str:
    v = VEHICLE_LOCK[vehicle_id]
    cond = state_override or resolve_vehicle_condition(vehicle_id, scene_num, clip_num)
    return (
        f"- {v['vehicle_id']} ({v['name']}): {v['model_silhouette']}; {v['exterior_color_material']}; "
        f"{v['wheels_axles']}; {v['lights_accessories']}; {v['interior_layout']}. Current state: {cond}."
    )


def format_object_lock_line(object_id: str, scene_num: int, clip_num: int, state_override: str = "") -> str:
    obj = OBJECT_LOCK[object_id]
    cond = state_override or resolve_object_condition(object_id, scene_num, clip_num)
    return f"- {obj['object_id']} ({obj['name']}): {obj['material_appearance']}. Current state: {cond}."


def select_relevant_bible_slice(plan: dict, shot: dict) -> dict[str, Any]:
    """Extract only the Film Bible entries relevant to `shot` (never dump the whole Bible)."""
    scene_num = shot.get("scene", 1)
    clip_num = shot.get("number", 1)
    loc_key = shot["location"]
    env = ENVIRONMENT_LOCK.get(loc_key, {})

    char_entries = []
    for look_key in shot.get("characters", []):
        base = plan["looks"][look_key][0]
        c_lock = CHARACTER_LOCK.get(base, {})
        char_entries.append({
            "look_key": look_key,
            "base": base,
            "lock": c_lock,
        })

    veh_entries = []
    obj_entries = []
    v_states = (shot.get("entity_state") or {}).get("vehicles") or {}
    o_states = (shot.get("entity_state") or {}).get("objects") or {}

    for p_key in shot.get("props", []):
        if p_key in VEHICLE_LOCK:
            veh_entries.append(
                format_vehicle_lock_line(p_key, scene_num, clip_num, v_states.get(p_key, ""))
            )
        elif p_key in OBJECT_LOCK:
            obj_entries.append(
                format_object_lock_line(p_key, scene_num, clip_num, o_states.get(p_key, ""))
            )

    physics_lines = []
    if veh_entries or env.get("category") in ("highway", "desert_airfield", "hillside_road", "rail_crossing", "vehicle_interior"):
        physics_lines.append(PHYSICS_RULES["vehicle"])
    if char_entries:
        physics_lines.append(PHYSICS_RULES["character"])
    if obj_entries:
        physics_lines.append(PHYSICS_RULES["hand_object"])
    physics_lines.append(PHYSICS_RULES["action_stunt"])
    physics_lines.append(PHYSICS_RULES["environment"])

    return {
        "environment": env,
        "characters": char_entries,
        "vehicle_lines": veh_entries,
        "object_lines": obj_entries,
        "physics_lines": physics_lines,
    }
