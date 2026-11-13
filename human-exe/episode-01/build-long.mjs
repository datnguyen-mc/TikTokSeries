import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const base=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(base,'../../.production-skills/directing-stickman-videos');
const require=createRequire(path.join(root,'package.json')),sharp=require('sharp');
const dir=path.join(base,'longform');fs.mkdirSync(path.join(dir,'art'),{recursive:true});
const story=JSON.parse(fs.readFileSync(path.join(base,'story-10min.json')));
const alignment=JSON.parse(fs.readFileSync(path.join(base,'words-10min.json')));
const words=alignment.words;
const ink='#202521',paper='#fdfdfc',blue='#4285ab',gold='#f1c75b',red='#e55c4d',green='#83a88a';
const P=(d,e='')=>`<path d="${d}" ${e}/>`;
const R=(x,y,w,h,fill='none',r=3)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" fill="${fill}"/>`;
const E=(x,y,rx,ry,e='')=>`<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" ${e}/>`;
const line=(d,color=ink,width=2.5)=>P(d,`stroke="${color}" stroke-width="${width}"`);
async function art(name,w,h,body){await sharp(Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}"><g fill="none" stroke="${ink}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">${body}</g></svg>`)).resize(w*2,h*2).png().toFile(path.join(dir,'art',name+'.png'));}
await art('machine',300,230,R(30,35,240,165,'#e9eff1',9)+R(52,60,194,60,paper,5)+P('M15 165 L64 165 L64 185 L15 185 Z',`fill="${gold}"`)+P('M237 156 L290 156 L290 177 L237 177 Z',`fill="${green}"`)+E(79,153,10,10,`fill="${blue}"`)+E(116,153,10,10,`fill="${gold}"`)+P('M178 153 L237 153 M180 169 L218 169')+P('M52 201 L52 220 M242 201 L242 220')+P('M80 89 L105 74 L129 96 L151 75 L172 94 L211 79',`stroke="${blue}"`));
await art('sandwich',210,160,P('M20 72 Q38 6 105 15 Q176 9 194 72 Z',`fill="#f4ce86"`)+P('M19 76 L194 76 L182 98 L29 100 Z',`fill="${green}"`)+P('M26 103 L184 103 L185 125 L28 129 Z',`fill="${gold}"`)+P('M27 133 L185 129 L178 148 L37 150 Z',`fill="#e2b475"`)+P('M67 38 L71 42 M101 33 L105 37 M139 42 L144 46','stroke-width="2"'));
await art('check',160,160,E(80,80,65,65,`fill="#e9f3e9" stroke="${green}"`)+P('M44 81 L69 106 L116 53',`stroke="${green}" stroke-width="8"`));
await art('cross',160,160,E(80,80,65,65,`fill="#fbe9e5" stroke="${red}"`)+P('M52 52 L108 108 M52 108 L108 52',`stroke="${red}" stroke-width="7"`));
await art('magnifier',180,200,E(73,73,57,57,`fill="#eaf3f5" fill-opacity=".55"`)+E(73,73,47,47)+P('M111 117 L165 182 L151 194 L99 128 Z',`fill="${gold}"`));
await art('bowl',220,150,P('M17 63 L203 63 Q189 138 111 138 Q36 134 17 63 Z',`fill="#e4eef4"`)+E(110,62,92,20,`fill="#f2dbad"`)+P('M45 52 Q64 34 82 57 M96 53 Q117 34 135 59 M143 49 Q165 32 183 58',`stroke="${green}"`)+P('M55 27 Q42 15 54 2 M98 25 Q84 13 98 0 M144 24 Q132 12 146 1','stroke="#a8b1a7" stroke-width="2"'));
await art('bowl-cold',220,150,P('M17 63 L203 63 Q189 138 111 138 Q36 134 17 63 Z',`fill="#e4eef4"`)+E(110,62,92,20,`fill="#d4ded5"`)+P('M45 52 Q64 34 82 57 M96 53 Q117 34 135 59 M143 49 Q165 32 183 58',`stroke="#879d8a"`));
await art('fridge',280,350,R(25,10,228,326,'#e8eeea',10)+R(42,32,194,284,paper,3)+P('M43 139 L234 139 M43 231 L234 231 M65 55 L65 104 M65 161 L65 207','stroke="#738d7e"'));
await art('phone',160,250,R(26,8,110,234,'#e3e9e4',13)+R(34,28,94,184,paper,5)+P('M64 18 L98 18')+E(81,230,5,5)+R(45,61,72,32,'#e8f0e5')+P('M52 72 L104 72 M52 83 L90 83','stroke-width="1.5"')+R(45,108,72,40,'#fff0c3')+P('M52 121 L108 121 M52 133 L93 133','stroke-width="1.5"'));
await art('battery',280,170,R(12,25,235,120,paper,9)+R(248,60,20,49,'#b7c6b8')+R(23,37,35,94,'#ec8f7b',2)+P('M133 51 L114 87 L139 87 L120 122',`stroke="${red}" stroke-width="4"`));
await art('battery-full',280,170,R(12,25,235,120,paper,9)+R(248,60,20,49,'#b7c6b8')+[0,1,2,3].map(i=>R(24+i*54,37,44,94,'#aecbab',2)).join(''));
await art('tray',280,150,P('M26 61 L246 61 L273 128 L5 128 Z',`fill="#f6edce"`)+P('M26 61 L26 22 L246 22 L246 61 M6 128 L6 145 L273 145 L273 128')+P('M91 91 L188 91','stroke="#8e927e"'));
await art('green-chart',300,220,R(8,8,284,204,paper)+P('M41 36 L41 177 L265 177','stroke="#6e7b6c"')+[0,1,2,3,4].map((i)=>R(61+i*39,150-i*24,24,27+i*24,green)).join(''));
await art('error-log',240,250,R(15,9,210,232,paper)+[0,1,2,3].map(i=>P(`M34 ${55+i*49} L45 ${66+i*49} M34 ${66+i*49} L45 ${55+i*49}`,`stroke="${red}"`)+P(`M65 ${57+i*49} L198 ${57+i*49} M65 ${70+i*49} L173 ${70+i*49}`,'stroke-width="1.6"')).join(''));
await art('gate',220,220,P('M25 211 L25 21 L187 21 L187 211 M43 211 L43 38 L169 38 L169 211')+P('M35 114 L177 114',`stroke="${red}" stroke-width="9"`)+E(106,114,24,24,`fill="#f8e4de"`)+P('M93 114 L119 114',`stroke="${red}" stroke-width="5"`));
await art('bench',380,210,P('M18 31 L359 31 L359 56 L18 56 Z M18 67 L359 67 L359 91 L18 91 Z M11 112 L367 112 L367 139 L11 139 Z',`fill="#d9b58a"`)+P('M48 93 L48 195 M321 93 L321 195 M37 197 L63 197 M309 197 L336 197'));
await art('tree',210,350,P('M91 180 L84 330 L121 330 L113 171',`fill="#d4b18a"`)+P('M102 15 Q158 0 166 50 Q213 55 192 102 Q216 142 166 164 Q147 212 102 184 Q50 208 36 160 Q1 159 14 109 Q-2 63 44 48 Q48 6 102 15 Z',`fill="#c8dcc2"`)+P('M103 269 L70 229 M105 218 L138 180'));
await art('standing',240,330,P('M105 1 Q94 73 112 148 M112 148 L63 302 M112 148 L172 303 M102 23 Q43 48 25 113 L72 145 M104 24 Q166 44 196 108 L157 143')+E(52,309,23,6,`fill="${paper}"`)+E(183,309,23,6,`fill="${paper}"`)+E(76,145,9,6,`fill="${paper}"`)+E(151,145,9,6,`fill="${paper}"`));
await art('pointing',240,330,P('M105 1 Q94 73 112 148 M112 148 L63 302 M112 148 L172 303 M102 23 Q43 48 25 113 L72 145 M105 23 L165 64 L223 25')+E(52,309,23,6,`fill="${paper}"`)+E(183,309,23,6,`fill="${paper}"`)+E(76,145,9,6,`fill="${paper}"`)+E(224,24,9,6,`fill="${paper}"`));
await art('table',650,210,P('M18 21 L624 21 L639 41 L5 41 Z',`fill="#f4efe0"`)+P('M27 42 L20 202 L34 202 L43 42 M595 42 L600 202 L614 202 L611 42'));
await art('cloud',320,180,P('M55 137 Q9 140 16 95 Q-1 48 55 43 Q70 -4 130 27 Q182 -4 216 38 Q276 19 281 70 Q330 108 283 139 Z',`fill="#edf1ee"`));
await art('question',180,200,P('M45 54 Q51 9 104 17 Q162 27 139 79 Q130 98 95 111 L92 139',`stroke="${blue}" stroke-width="15"`)+E(91,175,8,8,`fill="${blue}" stroke="none"`));
await art('loading',330,100,R(10,20,310,60,paper,5)+R(20,30,95,40,gold,3));
await art('blank-card',280,190,R(10,10,260,170,'#fff2c9',4));
await art('calendar-green',235,240,R(10,25,215,201,paper,4)+R(10,25,215,43,'#b5d0b7',4)+P('M57 10 L57 41 M116 10 L116 41 M173 10 L173 41')+[0,1,2].map(r=>[0,1,2,3].map(c=>R(30+c*47,91+r*40,28,23,'none',1)).join('')).join(''));
const legacy=new Set(['head-happy','head-worried','head-tired','ben-body','typing-arm','desk','report','sheet','email','presentation','timer','needle','mug','door','mara','laptop','calendar','stack']);
let ids=0;
const IMG=(name,x,y,w,h,keys,reason,role='prop')=>({type:'image',path:legacy.has(name)?`../art/${name}.png`:`art/${name}.png`,x,y,w,h,...(keys?{id:`local-${++ids}`,keys,motion:{role,reason}}:{})});
const TXT=(text,x,y,size=58,color=ink,w=1100)=>({type:'text',text,x,y,size,color,w,bold:true});
const HEAD=(mood,x,y,w=100,action=false,span=3)=>{
 const px=w*.53,py=w*1.0;
 const keys=action?[[0,0],[span*.40,-.08],[span*.85,.05]].map(([t,a])=>({t,angle:a,x:x+px-px*Math.cos(a)+py*Math.sin(a),y:y+py-px*Math.sin(a)-py*Math.cos(a)})):null;
 return IMG('head-'+mood,x,y,w,w*115/110,keys,'Ben looks between the empty tray and his screen while waiting','actor');
};
const STAND=(x,y,s=1,mood='happy',point=false)=>[IMG(point?'pointing':'standing',x,y+98*s,240*s,330*s),HEAD(mood,x+52*s,y,110*s)];
const DESK=(mood='happy',span=3)=>[IMG('ben-body',730,243,320,300),HEAD(mood,730,142,110),IMG('typing-arm',789,267,165,100,[{t:0,angle:0},{t:Math.min(.45,span*.3),angle:.045},{t:Math.min(1,span*.6),angle:0}],'Ben operates the keyboard while reviewing his work','actor'),IMG('desk',850,200,410,310)];
const ARROW=(x,y,w=160)=>({type:'arrow',x,y,w,color:'#7b8f7e'});
const NEEDLE=(span)=>{
 const x=260,y=300,px=80,py=100;
 const keys=[[0,-1.2],[Math.min(1.4,span*.4),.1],[Math.max(.1,span*.85),.6]].map(([t,a])=>({t,angle:a,x:x+px-px*Math.cos(a)+py*Math.sin(a),y:y+py-px*Math.sin(a)-py*Math.cos(a)}));
 return IMG('needle',x,y,160,190,keys,'The stopwatch hand rotates around its fixed center to illustrate time');
};
const principal=(name,x,y,w,h,span,reason,mode='arrive')=>{
 const settle=Math.min(1.2,span*.42),reveal=Math.min(span-.05,Math.max(settle+.1,span*.80));
 let keys;
 if(mode==='scan') keys=[{t:0,x:x-55,y},{t:settle,x:x+55,y:y-15},{t:reveal,x:x+15,y:y+20}];
 else if(mode==='carry') keys=[{t:0,x:x-85,y:y+15},{t:settle,x,y},{t:reveal,x:x+55,y:y-5}];
 else if(mode==='lower') keys=[{t:0,x,y:y-65},{t:settle,x,y},{t:reveal,x,y:y+18}];
 else if(mode==='reveal') keys=[{t:0,x:x+80,y:y+24},{t:settle,x,y},{t:reveal,x:x-25,y:y-12}];
 else keys=[{t:0,x:x-80,y:y+28},{t:settle,x,y},{t:reveal,x:x+20,y:y-8}];
 return IMG(name,x,y,w,h,keys,reason);
};
// Acoustic word timing is source-matched by align-long.py. Keep sentence and
// clause captions intact where they fit, then prefer grammar/pause boundaries.
const prohibited=new Set(['a','an','the','to','of','for','in','on','at','with','his','her','their','my','our','this','that','these','those','and','or','but','because','if']);
function captionGroups(ws){
 if(ws.map(w=>w.word).join(' ').length<=66) return [ws];
 let best=-1,bscore=-1e6;
 for(let i=2;i<ws.length-1;i++){
  const left=ws.slice(0,i).map(w=>w.word).join(' '),right=ws.slice(i).map(w=>w.word).join(' '),prev=ws[i-1].word.replace(/[^a-z]/gi,'').toLowerCase(),next=ws[i].word.toLowerCase();
  if(prohibited.has(prev))continue;
  let score=-Math.abs(left.length-right.length)*.1 + Math.min(.5,Math.max(0,ws[i].start-ws[i-1].end))*20;
  if(/[,;:]$/.test(ws[i-1].word))score+=14;
  if(/^(and|but|while|when|because|instead|which|without|before|after|that|where)$/.test(next))score+=7;
  if(left.length<=66&&right.length<=66)score+=8;
  if(score>bscore){best=i;bscore=score;}
 }
 if(best<0)throw Error('Cannot find a readable caption phrase');
 return [...captionGroups(ws.slice(0,best)),...captionGroups(ws.slice(best))];
}
const sentences=[];let cursor=0;
story.beats.forEach((beat,bi)=>{
 const pieces=beat.text.match(/[^.!?]+[.!?]+|[^.!?]+$/g).map(x=>x.trim()).filter(Boolean);
 pieces.forEach((sentence,si)=>{
  const n=sentence.split(/\s+/).length, ws=words.slice(cursor,cursor+n);
  if(ws.map(x=>x.word).join(' ')!==sentence)throw Error('Source sentence mismatch '+bi+':'+si);
  sentences.push({bi,si,beat,sentence,words:ws,start:ws[0].start,end:ws.at(-1).end});cursor+=n;
 });
});
if(cursor!==words.length)throw Error('Source timing count mismatch');
const captions=[];
for(const s of sentences)for(const group of captionGroups(s.words))captions.push({start:group[0].start,end:Math.max(group.at(-1).end,group[0].start+.12),text:group.map(x=>x.word).join(' ')});
// Resolve sub-word timestamp overlap introduced by rare ASR substitutions.
for(let i=1;i<captions.length;i++)captions[i-1].end=Math.min(captions[i-1].end,captions[i].start);
const select=(scene,i,text)=>{
 const t=text.toLowerCase();
 const planned={
  printer:[['transfer','email','sheet','SAME DATA. NEW RECTANGLE.'],['files','report','presentation','FINAL.'],['files','report','presentation','FINAL TWO.'],['files','report','presentation','ACTUALLY FINAL.'],['files','report','calendar','A FAMILY OF FILES']],
  workflow:[['desk','report','machine','A SMALL EXPERIMENT'],['workflow','email','machine','DUMMY DATA. REAL TEST.'],['transfer','email','tray','SORT THE MESSAGES'],['review','sheet','magnifier','EXTRACT THE DETAILS'],['desk','report','machine','DRAFT THE REPORT'],['review','gate','report','STOP FOR A HUMAN CHECK'],['review','question','report','A PERSON STILL DECIDES'],['transfer','email','report','LESS COPYING. MORE THINKING.']],
  timer:[['desk','report','machine','BEFORE THE COFFEE COOLED'],['review','sheet','magnifier','CHECK THE TOTALS'],['pair','sheet','check','CORRECT.'],['review','report','magnifier','CHECK THE ATTACHMENTS'],['pair','report','check','CORRECT.'],['headspace','question','cloud','ALLOWED TO FEEL HAPPY?'],['headspace','question','cloud','UNCLEAR.'],['emptytray','tray','report','WAITING...'],['emptytray','tray','report','NOTHING.'],['quiet','machine','check','THE FACTORY WAS QUIET'],['headspace','cloud','cloud','SO WAS HIS HEAD']],
  stack:[['desk','report','machine','SAME DESK.'],['salary','blank-card','report','SAME SALARY.'],['pair','report','stack','BIGGER RECTANGLE.'],['calendar','calendar','question','JUST TEMPORARY?'],['workflow','machine','report','FINISH THE NEW BATCH'],['pair','blank-card','stack','ANOTHER DEPARTMENT'],['queues','tray','stack','A LONGER QUEUE'],['review','machine','check','ANOTHER IMPROVEMENT'],['load','stack','tray','MORE WORK ARRIVED'],['workflow','machine','stack','EFFICIENCY IN. OBLIGATIONS OUT.']]
 };
 if(planned[scene]?.[i])return planned[scene][i];
 if(scene==='exception'&&i===6)return ['cold','fridge','bowl-cold','LUNCH CAN WAIT. AGAIN.'];
 if(scene==='battery'&&i===0)return ['missedwalk','tree','bench','NO WALK TODAY'];
 if(scene==='doublebelt'&&i===5)return ['calendar','calendar','question','LUNCH: TENTATIVE'];
 if(scene==='meeting'&&i===5)return ['doublebelt','machine','machine','SHE WAS IN THE MACHINE TOO'];
 if(scene==='meeting'&&i===6)return ['doublebelt','machine','stack','THE NEXT CONVEYOR BELT'];
 if(scene==='boundary'&&i===0)return ['review','gate','report','THE FIRST TEST'];
 if(scene==='balance'&&i===0)return ['choices','blank-card','calendar-green','OUTPUT IS A CHOICE'];
 if(scene==='results'&&i===6)return ['review','gate','check','EFFICIENCY HAS A LIMIT'];
 if(/sandwich/.test(t))return ['pair','sandwich','report','WRONG CATEGORY'];
 if(/tuesday/.test(t))return ['pair','green-chart','question','TUESDAY +12%?'];
 if(/customer called/.test(t))return ['card','blank-card','question','CUSTOMER'];
 if(/mother|phone|message saying|phone lit/.test(t))return ['pair','phone','calendar','CALL LATER?'];
 if(/warm lunch|lunch was warm|took a real lunch|cook|adding water/.test(t))return ['lunch','bowl','battery-full','A REAL BREAK'];
 if(/daylight|went outside|walked outside/.test(t))return ['outside','tree','bench','AFTER WORK'];
 if(/error log|corrected|correction|mistake/.test(t))return ['review','error-log','magnifier','LOOK CLOSER'];
 if(/quality|checks|review|inspect|strange totals/.test(t))return ['review','report','magnifier','HUMAN REVIEW'];
 if(/green|dashboard|number/.test(t))return ['pair','green-chart','error-log','WHAT GETS COUNTED?'];
 if(/eight hours|twelve minutes|twenty minutes|forty minutes/.test(t))return ['clock','timer','needle','TIME AT WORK'];
 if(/more output|more work|three people|three people's|another department/.test(t))return ['load','stack','tray','MORE WORK'];
 if(/time back|saved time|saved hour|time afterward/.test(t))return ['pair','calendar-green','calendar','WHO GETS THE TIME?'];
 if(/decision|choose|choice|agreement/.test(t))return ['choices','blank-card','calendar-green','MAKE THE CHOICE'];
 if(/meeting|conversation/.test(t))return ['meeting','table','report','LET\'S TALK'];
 if(/calendar|schedule|one month|every week/.test(t))return ['calendar','calendar-green','report','MAKE ROOM'];
 if(/exception|unusual|judgment|question/.test(t))return ['review','question','report','THIS NEEDS A PERSON'];
 if(/loading|progress bar|slower|processing|curtain/.test(t))return ['loading','loading','laptop','LOOKING BUSY'];
 if(/energy|recover|finish line/.test(t))return ['pair','battery','battery-full','RUNNING LOW'];
 if(/jo|coworker|documented|knowledge/.test(t))return ['team','report','check','SHARED KNOWLEDGE'];
 const plans={
  printer:['transfer','report','presentation','ANOTHER RECTANGLE'],clock:['clock','timer','needle','BUSY ENOUGH?'],workflow:['workflow','email','machine','TEST. CHECK. FIX.'],error:['pair','report','cross','CONFIDENTLY WRONG'],check:['review','report','magnifier','KEEP THE CHECKS'],timer:['clock','timer','needle','TWELVE MINUTES'],lunch:['lunch','bowl','phone','TIME BACK'],calendar:['calendar','calendar-green','report','PREVENT TOMORROW\'S MISTAKE'],boss:['boss','mara','machine','HIS BOSS NOTICED'],reward:['load','stack','tray','GREAT WORK!'],stack:['load','stack','report','SAME DESK. BIGGER PILE.'],factory:['workflow','machine','stack','THE NEW NORMAL'],exception:['review','gate','report','STOP AND THINK'],chart:['pair','green-chart','error-log','WHAT THE NUMBER MISSED'],coworker:['loading','loading','laptop','THE ADVICE'],battery:['pair','battery','calendar','THE MISSING HOURS'],meeting:['meeting','table','laptop','THE OTHER SECRET'],doublebelt:['workflow','machine','stack','SAME TRAP'],choices:['choices','blank-card','calendar-green','THREE POSSIBILITIES'],balance:['choices','blank-card','check','A REAL TRADEOFF'],proposal:['meeting','table','error-log','THE FIRST PROPOSAL'],evidence:['pair','green-chart','error-log','WHAT THE NUMBER MISSED'],trial:['calendar','calendar-green','check','ONE MONTH'],boundary:['review','gate','report','WHICH TASK SHOULD MOVE?'],team:['team','report','check','SHARED KNOWLEDGE'],results:['pair','battery-full','check','A DIFFERENT RESULT'],reflection:['choices','calendar-green','question','WHO DECIDES?'],ending:['outside','tree','bench','THE ACTUAL UPGRADE']
 };
 return plans[scene]??['desk','report','machine','ONE CLICK.'];
};
function compose(s,span){
 const {beat,si,sentence}=s,[kind,a,b,title]=select(beat.scene,si,sentence),m=beat.mood;
 const top=[TXT(beat.heading,75,55,34,'#687769')];
 const mode=si%2?'reveal':'carry';
 let layers=[];
 if(kind==='headspace'){
  layers=[...top,TXT(title,75,137,64),IMG('head-'+m,820,270,240,251),principal(a,385,285,230,190,span,'A thought leaves or enters Ben\'s attention as described by the narration','carry')];
 }else if(kind==='files'){
  layers=[...top,TXT(title,75,135,69),...['FINAL','FINAL 2','ACTUALLY FINAL'].flatMap((label,j)=>[principal('report',190+j*320,300,160,193,span,'Another version of the same document is added to the file family',j%2?'reveal':'carry'),TXT(label,180+j*320,520,31,ink,270)])];
 }else if(kind==='emptytray'){
  layers=[...top,TXT(title,75,135,70),IMG('tray',330,365,280,150),IMG('standing',875,155+98*.83,240*.83,330*.83),HEAD('happy',875+52*.83,155,110*.83,true,span)];
 }else if(kind==='quiet'){
  layers=[...top,TXT(title,75,135,65),IMG('machine',320,290,300,230),principal('check',770,300,160,160,span,'The completed-work status settles while the machine has no new input','reveal')];
 }else if(kind==='salary'){
  layers=[...top,TXT(title,75,135,69),IMG('blank-card',235,290,360,245),TXT('UNCHANGED',270,382,50,ink,300),...STAND(855,170,.8,'tired'),principal('report',635,330,140,169,span,'The unchanged pay statement is presented for comparison','carry')];
 }else if(kind==='queues'){
  layers=[...top,TXT(title,75,135,68),IMG('tray',205,390,280,150),IMG('tray',800,390,280,150),principal('stack',210,230,240,210,span,'The short queue is replaced by a larger pile','lower'),principal('stack',820,230,240,210,span,'A second queue is introduced as the workload spreads','reveal')];
 }else if(kind==='cold'){
  layers=[...top,TXT(title,75,135,65),IMG('fridge',785,195,280,350),principal('bowl-cold',790,322,160,109,span,'The unsteaming cold lunch is returned onto the fridge shelf','carry'),...STAND(190,205,.70,'tired')];
 }else if(kind==='missedwalk'){
  layers=[...top,TXT(title,75,135,65,red),IMG('tree',300,225,180,300),IMG('bench',380,340,330,182),...DESK('tired',span),principal('cross',445,330,160,160,span,'The crossed-out walk shows the break Ben stopped taking','lower')];
 }else if(kind==='doublebelt'){
  layers=[...top,TXT(title,75,135,64),IMG('machine',150,300,300,230),IMG('machine',830,300,300,230),principal('report',500,310,160,193,span,'Work moves from one level of the organization to the next','carry'),IMG('head-tired',230,220,95,99),IMG('mara',900,130,130,298)];
 }else if(kind==='desk'||kind==='load'||kind==='boss'){
  layers=[...top,TXT(title,75,145,65,kind==='load'?red:ink,580),...DESK(m,span),principal(a==='mara'?'report':a,995,220,205,180,span,'The current work item reaches Ben\'s desk',kind==='load'?'lower':mode)];
  if(kind==='boss')layers.splice(2,0,IMG('door',1090,40,150,430),principal('mara',1070,50,175,402,span,'Mara approaches Ben to look at the workflow','reveal'));
 }else if(kind==='outside'){
  layers=[...top,TXT(title,75,135,64,blue),IMG('tree',1015,180,190,317),IMG('bench',730,350,340,188),...STAND(520,225,.70,m),principal('phone',280,320,100,156,span,'A phone insert contrasts notifications with Ben\'s time outside','lower')];
 }else if(kind==='lunch'){
  layers=[...top,TXT(title,75,140,67),...STAND(840,140,.82,m),IMG('table',425,380,620,201),principal('bowl',600,250,220,150,span,'A warm lunch is placed on the table','lower')];
 }else if(kind==='meeting'||kind==='team'){
  layers=[...top,TXT(title,75,128,61),...STAND(260,235,.65,m,true),IMG('mara',900,235,145,333),IMG('table',350,375,620,201),principal(b,590,260,170,165,span,'The team places the relevant evidence on the meeting table','lower')];
 }else if(kind==='workflow'){
  layers=[...top,TXT(title,75,128,64),IMG('machine',490,270,300,230),ARROW(345,385,120),ARROW(800,385,100),principal(a==='machine'?'email':a,175,315,150,145,span,'The source item moves into the workflow','carry'),principal(b==='machine'?'report':b,940,300,165,165,span,'The workflow delivers an item that still needs review','reveal')];
 }else if(kind==='review'){
  layers=[...top,TXT(title,75,125,64),...STAND(880,150,.83,m,true),IMG(a,275,280,235,245),principal(b==='magnifier'?'magnifier':b,470,300,175,180,span,'A person inspects the relevant exception before it is released','scan')];
 }else if(kind==='clock'){
  layers=[...top,TXT(title,75,130,65),IMG('timer',220,250,240,270),NEEDLE(span),...STAND(820,155,.85,m)];
 }else if(kind==='choices'){
  layers=[...top,TXT(title,75,126,65),...['MORE OUTPUT','BETTER QUALITY','TIME BACK'].flatMap((label,j)=>[principal('blank-card',95+j*380,300,280,190,span,'An explicit alternative is brought into the decision',j%2?'reveal':'lower'),TXT(label,115+j*380,356,35,j===2?blue:ink,230)])];
 }else if(kind==='calendar'){
  layers=[...top,TXT(title,75,128,62),...STAND(900,155,.8,m,true),IMG(a,200,265,235,240),principal(b,490,310,190,175,span,'A protected calendar decision is made visible','carry')];
 }else if(kind==='loading'){
  layers=[...top,TXT(title,75,135,65),IMG('laptop',200,280,370,250),principal('loading',655,340,330,100,span,'The progress indicator makes the deliberate delay visible','reveal'),...STAND(1000,175,.7,m)];
 }else if(kind==='card'){
  layers=[...top,TXT(title,75,135,68),principal(a,230,285,360,245,span,'The suspicious customer record is brought forward for inspection','reveal'),TXT('Customer',270,365,54),principal('question',850,300,140,155,span,'The implausible record prompts a question','lower')];
 }else{
  layers=[...top,TXT(title,75,128,64,ink),principal(a,190,300,240,210,span,'The first item is moved into the comparison',mode),ARROW(530,395,165),principal(b,865,300,240,210,span,'The consequence or comparison is revealed','reveal')];
 }
 return {layers,kind,reason:sentence};
}
const shots=[],ledger=[];let index=0;
for(const s of sentences){
 const start=index===0?0:sentences[index].start;
 const end=index===sentences.length-1?603.5025:sentences[index+1].start;
 const span=end-start;
 if(span<.12)throw Error('Invalid sentence interval '+index);
 const comp=compose(s,span);
 shots.push({start,end,layers:comp.layers});
 ledger.push({shot:index+1,start,end,beat:s.bi+1,sentence:s.sentence,kind:comp.kind,focal_action:comp.reason,caption_indices:captions.flatMap((c,i)=>c.start>=start-.001&&c.start<end?[i]:[]),review:'pending encoded picture/sound review'});
 index++;
}
// Reuse the opening's authored shot grammar, matched to this recording's actual
// first-paragraph boundary. Other scenes are authored for the expanded story.
const opening=JSON.parse(fs.readFileSync(path.join(base,'project.json')));
const boundary=sentences.find(s=>s.bi===1).start;
const openingShots=structuredClone(opening.shots);
for(const s of openingShots)for(const l of s.layers)if(l.path)l.path='../'+l.path;
openingShots.at(-1).end=boundary;
if(boundary>21.8){const l=openingShots.at(-1).layers.find(l=>l.path?.includes('presentation'));if(l?.keys)l.keys.push({t:boundary-openingShots.at(-1).start-.1,y:280});}
const cut=shots.findIndex(s=>s.start>=boundary-.001);
shots.splice(0,cut,...openingShots);
const sfx=[];
for(const [i,s] of shots.entries()){
 const span=s.end-s.start;
 if(i<9)continue;
 const phrase=sentences.find(t=>t.start>=s.start-.01&&t.start<s.end)?.sentence.toLowerCase()??'';
 let kind=null;
 if(/report|paper|calendar|document|slide|proposal|rectangle/.test(phrase))kind='paper';
 else if(/button|press|workflow|computer|laptop/.test(phrase))kind='tap';
 else if(/correct|agreed|warm|choice/.test(phrase))kind='chime';
 if(kind)sfx.push({time:s.start+Math.min(.6,span*.3),kind,gain:kind==='chime'?.014:.022});
}
sfx.unshift(...opening.sfx);
const project={version:1,style:'B1',width:1280,height:720,fps:30,voice:{path:'../narration-10min.wav',lead:0,tail:.4975},captions,shots,sfx,ambience:[{path:'../office-bed.wav',start:0,end:604,gain:.055,loop:true,fadeIn:.05,fadeOut:.4}],reference_review:{author_id:'codex-longform-production',capability:{mode:'limited',environment:'Workspace-local B1 runtime; original layered artwork; macOS Samantha; local acoustic word timestamps',limitations:[{capability:'voice',observed:'User selected free installed macOS voice and then requested a ten-minute version.',impact:'OS narration; no match to Gemini Bodi claimed.'},{capability:'independent audible reference playback',observed:'Normal-speed comparative listening is unavailable in this toolchain.',impact:'Encoded film will remain pending independent creative/listening review; no fabricated acceptance.'}]}}};
shots.at(-1).end=604;
fs.writeFileSync(path.join(dir,'project.json'),JSON.stringify(project,null,2));
const finalLedger=shots.map((s,i)=>{
 const source=sentences.find(q=>q.start>=s.start-.001&&q.start<s.end)??sentences.findLast(q=>q.start<=s.start);
 return {shot:i+1,start:s.start,end:s.end,beat:source.bi+1,spoken_text:captions.filter(c=>c.start>=s.start-.001&&c.start<s.end).map(c=>c.text).join(' '),source_sentence:source.sentence,layers:s.layers.filter(l=>l.motion).map(l=>({id:l.id,role:l.motion.role,reason:l.motion.reason,keys:l.keys})),review:'pending encoded picture/sound review'};
});
fs.writeFileSync(path.join(dir,'shot-ledger.json'),JSON.stringify(finalLedger,null,2));
fs.writeFileSync(path.join(dir,'sound-script.json'),JSON.stringify(story.beats.map((b,i)=>({beat:i+1,exact_text:b.text,scene:b.scene,bed:'Quiet designed office bed; outdoor scenes use a subtle neutral bed, not a real field recording',events:sfx.filter(f=>f.time>=sentences.find(s=>s.bi===i).start&&f.time<((sentences.find(s=>s.bi===i+1)?.start)??604)),rights:'Original project drawings; upstream original procedural effects; generated noise bed',voice:'macOS Samantha; native rate unchanged'})),null,2));
console.log(JSON.stringify({project:path.join(dir,'project.json'),sentences:sentences.length,shots:shots.length,captions:captions.length,duration:604}));
