import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
const base=path.dirname(fileURLToPath(import.meta.url));
const runtime=path.resolve(base,'../../.production-skills/directing-stickman-videos');
const require=createRequire(path.join(runtime,'package.json'));
const sharp=require('sharp');
fs.mkdirSync(path.join(base,'art'),{recursive:true});
const ink='#202521', blue='#4285ab', gold='#f1c75b', red='#e55c4d', paper='#fdfdfc';
const P=(d,extra='')=>`<path d="${d}" ${extra}/>`;
const E=(cx,cy,rx,ry,extra='')=>`<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" ${extra}/>`;
const R=(x,y,w,h,fill='none',r=2)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" fill="${fill}"/>`;
async function asset(name,w,h,body){
 const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}"><g stroke="${ink}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none">${body}</g></svg>`;
 await sharp(Buffer.from(svg)).resize(w*2,h*2).png().toFile(path.join(base,'art',name+'.png'));
}
const face=(mood)=>{
 let eyes=E(40,58,3.1,6,`fill="${ink}"`)+E(66,55,3.1,6,`fill="${ink}"`), brows='',mouth='';
 if(mood==='happy'){brows=P('M32 43 Q39 36 46 41 M58 38 Q66 33 73 39');mouth=P('M35 73 Q55 94 77 68 Q60 102 35 73',`fill="${paper}"`);}
 if(mood==='worried'){brows=P('M31 43 L46 36 M59 34 L77 42');mouth=P('M37 82 Q53 66 74 79 L72 89 Q54 81 37 82',`fill="${paper}"`);}
 if(mood==='tired'){eyes=P('M33 57 L47 59 M60 54 L74 57');brows=P('M31 44 L47 47 M59 43 L76 46');mouth=P('M42 80 Q57 73 72 81');}
 return E(55,58,45,45,`fill="${paper}"`)+P('M35 12 Q33 3 24 3 M40 11 Q48 0 57 5 M49 13 Q62 4 70 10')+eyes+brows+mouth;
};
await asset('head-happy',110,115,face('happy'));
await asset('head-worried',110,115,face('worried')+P('M94 28 Q105 39 99 43 Q91 41 94 28',`stroke="${blue}" fill="#d9eaf0"`));
await asset('head-tired',110,115,face('tired'));
await asset('ben-body',320,300,
 P('M58 42 Q20 39 24 93 L24 139 Q25 152 58 155 L125 155 M28 155 L13 240 M111 155 L130 240 M3 246 L148 246')+
 P('M57 2 Q65 64 87 136 M87 136 L183 149 L200 260 M87 136 L123 177 L88 262')+
 E(205,266,19,5,`fill="${paper}"`)+E(77,267,21,5,`fill="${paper}"`)+
 P('M67 24 Q32 73 48 103 L115 101')+E(119,101,9,5,`fill="${paper}"`));
await asset('typing-arm',165,100,P('M5 5 Q25 48 56 78 L148 76')+E(151,76,10,5,`fill="${paper}"`)+P('M137 70 L136 83',`stroke="${blue}" stroke-width="6"`));
await asset('desk',410,310,
 R(166,8,188,119,paper,5)+R(174,16,172,97,'#edf2ee',2)+P('M186 32 L235 32 M186 44 L290 44 M186 57 L267 57 M186 70 L317 70 M186 83 L250 83', 'stroke="#87978d" stroke-width="2"')+
 P('M252 127 L252 146 M226 147 L281 147')+P('M9 153 L390 153 L380 166 L0 166 Z',`fill="${paper}"`)+
 P('M14 167 L9 296 L21 296 L27 167 M367 168 L365 296 L378 296 L381 168')+
 P('M24 131 L137 131 L151 149 L13 149 Z',`fill="#f0f0eb"`)+
 P('M31 137 L128 137 M24 143 L138 143 M42 132 L37 147 M59 132 L56 147 M76 132 L75 147 M94 132 L94 147 M110 132 L115 147','stroke-width="1"')+
 E(165,142,12,7,`fill="${paper}"`)+P('M166 135 L166 140')+
 P('M1 153 L391 153','stroke-width="3"'));
await asset('report',145,175,P('M15 7 L110 7 L134 31 L134 165 L15 165 Z',`fill="#fff3cc"`)+P('M110 7 L109 32 L134 31')+P('M33 44 L91 44 M33 58 L115 58 M33 71 L111 71 M33 116 L113 116 M33 132 L106 132 M33 146 L96 146','stroke="#717b70" stroke-width="2"')+P('M36 104 L51 86 L70 94 L91 77 L110 85',`stroke="${blue}"`));
await asset('sheet',190,160,R(8,8,174,144,'#e5f0e7',3)+R(8,8,174,28,'#bad0bd',3)+P('M43 37 L43 150 M78 37 L78 150 M113 37 L113 150 M148 37 L148 150 M10 65 L180 65 M10 94 L180 94 M10 122 L180 122','stroke="#6e8f79" stroke-width="1.5"')+P('M22 21 L87 21','stroke="#597562"'));
await asset('email',190,150,R(8,20,174,117,'#e7eef4',5)+P('M10 24 L94 86 L179 24 M12 132 L68 76 M178 132 L122 77')+E(157,24,17,17,`fill="${gold}"`));
await asset('presentation',250,200,R(9,12,232,142,paper,3)+P('M125 155 L125 187 M125 165 L76 195 M125 165 L174 195')+R(26,30,87,77,'#e5f0e7')+P('M26 49 L113 49 M26 67 L113 67 M26 85 L113 85 M55 30 L55 107 M83 30 L83 107','stroke="#8fa994" stroke-width="1.3"')+P('M139 42 L219 42 M139 61 L210 61 M139 80 L218 80 M30 126 L218 126'));
await asset('timer',240,270,E(120,150,93,93,`fill="${paper}"`)+R(102,18,36,18,gold)+P('M111 36 L111 55 M129 36 L129 55 M183 70 L200 50 L213 61 L196 80')+Array.from({length:12},(_,i)=>{const a=i*Math.PI/6;return P(`M${120+Math.sin(a)*80} ${150-Math.cos(a)*80} L${120+Math.sin(a)*88} ${150-Math.cos(a)*88}`);}).join('')+E(120,150,5,5,`fill="${ink}"`));
await asset('needle',160,190,P('M80 100 L80 18',`stroke="${red}" stroke-width="4"`)+E(80,100,5,5,`fill="${ink}"`));
await asset('mug',65,75,P('M9 19 L43 19 L40 66 L13 66 Z',`fill="${gold}"`)+P('M44 26 Q70 22 59 47 L42 49 M18 10 Q10 2 19 0 M32 10 Q24 2 33 0','stroke-width="2"'));
await asset('door',170,430,P('M8 421 L8 9 L155 9 L155 421 M19 420 L19 25 L139 25 L139 420')+E(122,218,4,4,`fill="${gold}"`));
await asset('mara',170,390,E(81,59,38,40,`fill="${paper}"`)+P('M45 62 Q23 14 72 15 Q127 9 127 78 L103 75 M62 101 L65 210 M65 210 L31 363 M65 210 L119 364 M63 124 L20 180 L38 228 M65 124 L128 158 L142 118')+E(58,58,2.5,4,`fill="${ink}"`)+E(78,58,2.5,4,`fill="${ink}"`)+P('M52 45 L65 42 M72 43 L84 46 M57 77 Q72 86 84 74')+E(107,81,4,6,`fill="${gold}"`)+E(25,369,19,5,`fill="${paper}"`)+E(125,370,19,5,`fill="${paper}"`));
await asset('laptop',370,250,P('M27 15 L337 15 L323 208 L42 208 Z',`fill="#e6e9e5"`)+P('M42 208 L323 208 L359 233 L8 233 Z',`fill="${paper}"`)+E(182,105,15,15,`fill="${gold}"`));
await asset('calendar',235,240,R(10,25,215,201,paper,4)+R(10,25,215,43,'#f6d16c',4)+P('M57 10 L57 41 M116 10 L116 41 M173 10 L173 41')+Array.from({length:3},(_,r)=>Array.from({length:4},(_,c)=>R(30+c*47,91+r*40,28,23,'none',1)).join('')).join(''));
await asset('stack',240,210,Array.from({length:6},(_,i)=>P(`M${14+i*3} ${160-i*22} L${217-i*2} ${153-i*22} L${224-i*2} ${172-i*22} L${17+i*3} ${180-i*22} Z`,`fill="${i%2?'#fff3cc':paper}"`)).join(''));
const captions=[
 [0,1.85,'Ben automated his entire job.'],[1.92,2.72,'By Monday,'],[2.775,4.70,'he was working twelve minutes a day.'],
 [4.768,5.68,'By Friday,'],[5.734,7.76,'his boss wanted to know his secret.'],[7.808,9.04,'That was the problem.'],
 [9.098,10.36,'Three weeks earlier,'],[10.413,13.62,"Ben's job had been moving information between rectangles."],
 [13.684,15.65,'An email became a spreadsheet.'],[15.711,17.61,'The spreadsheet became a report.'],[17.671,20.925,'The report became a presentation explaining the spreadsheet.']
].map(([start,end,text])=>({start,end,text}));
// Captions use actual phrase boundaries detected in the continuous recording,
// not duration distributed across words. Sentence 8 is regrouped below after
// word-alignment inspection, while keeping the complete spoken text.
const T=(text,x,y,size=68,color=ink)=>({type:'text',text,x,y,size,bold:true,color,w:580});
let seq=0;
const I=(name,x,y,w,h,keys,reason,role='prop',extra={})=>{
 const {pivotX=0,pivotY=0,...rest}=extra;
 if(keys&&(pivotX||pivotY)) keys=keys.map(k=>{const a=k.angle??0;return {...k,x:(k.x??x)+pivotX-pivotX*Math.cos(a)+pivotY*Math.sin(a),y:(k.y??y)+pivotY-pivotX*Math.sin(a)-pivotY*Math.cos(a)};});
 return {type:'image',path:`art/${name}.png`,x,y,w,h,...rest,...(keys?{id:`action-${++seq}`,keys,motion:{role,reason}}:{})};
};
const head=(mood='happy',keys)=>I('head-'+mood,730,142,110,115,keys,'Ben reacts with a head turn to the current event','actor',{pivotX:58,pivotY:110});
const body=()=>I('ben-body',730,243,320,300);
const desk=()=>I('desk',850,200,410,310);
const arm=(press=false)=>I('typing-arm',789,267,165,100,[{t:0,angle:0},{t:.35,angle:press?.05:0},{t:.65,angle:0},{t:1.2,angle:press?.035:0},{t:1.5,angle:0}], 'Ben presses the keyboard; his arm pivots from his shoulder','actor');
const shots=[];
shots.push({start:0,end:1.92,layers:[T('ONE CLICK.',90,160,87),T('A whole job.',95,250,43,'#6a786c'),body(),head('happy'),arm(true),desk(),I('mug',911,306,38,44),I('report',1090,310,85,103,[{t:0,x:1090,y:310},{t:.75,x:1075,y:220},{t:1.3,x:1115,y:200}],'The completed report ejects after Ben presses the key')]});
shots.push({start:1.92,end:4.768,layers:[T('12 MINUTES.',75,126,80),I('timer',142,235,240,270),I('needle',182,285,160,190,[{t:0,angle:-1.8},{t:1.4,angle:.1},{t:2.35,angle:.6}],'The stopwatch hand sweeps to show the short working day','information',{pivotX:80,pivotY:100}),body(),head('happy',[{t:0,angle:0},{t:1,angle:-.08},{t:2,angle:0}]),I('typing-arm',789,267,165,100),desk(),I('mug',911,306,38,44)]});
shots.push({start:4.768,end:7.808,layers:[T('HIS BOSS',80,150,79),T('NOTICED.',80,245,79,red),I('door',1090,40,150,430),I('mara',1180,75,150,344,[{t:0,x:1180},{t:1.3,x:1080},{t:2.3,x:1055}],'Mara enters through the doorway to inspect the work','actor'),body(),head('worried',[{t:0,angle:-.05},{t:.65,angle:.09},{t:1.5,angle:.02}]),I('typing-arm',789,267,165,100,[{t:0,angle:0},{t:1.1,angle:.7},{t:1.7,angle:.7}],'Ben lowers the coffee toward his lap, keeping his hand on the handle','actor'),desk(),I('mug',911,315,38,44,[{t:0,x:911,y:315},{t:1.1,x:826,y:394},{t:1.7,x:826,y:394}],'The coffee follows Ben’s hand down to his lap')]});
shots.push({start:7.808,end:9.098,layers:[T('THAT WAS',80,170,75),T('THE PROBLEM.',80,265,75,red),I('head-worried',785,98,235,246,[{t:0,angle:0},{t:.6,angle:-.075},{t:1.2,angle:.025}],'Ben looks away from his boss nervously','actor',{pivotX:118,pivotY:234}),I('laptop',712,350,370,250,[{t:0,y:365},{t:.7,y:335}],'Ben raises the laptop to conceal his coffee')]});
shots.push({start:9.098,end:10.413,layers:[T('3 WEEKS',95,180,82),T('EARLIER...',95,270,76,'#657467'),I('calendar',800,175,235,240,[{t:0,angle:.1,x:850},{t:.6,angle:-.08,x:790},{t:1.2,angle:0,x:800}],'The calendar page turns back to establish the flashback','information')]});
shots.push({start:10.413,end:13.684,layers:[T('MOVING DATA.',70,165,72),T('ALL DAY.',75,255,74,blue),body(),head('tired',[{t:0,angle:0},{t:1.2,angle:.11},{t:2.4,angle:.02}]),desk(),I('stack',990,170,240,210,[{t:0,y:100},{t:.8,y:153},{t:1.6,y:170},{t:2.7,y:185}],'A heavy stack of paper settles on the desk as Ben slumps')]});
const transfer=(start,end,left,right,title,sub)=>({start,end,layers:[{...T(title,80,105,62),w:1120},T(sub,85,200,39,'#6a786c'),I(left,180,310,190,175,[{t:0,x:180},{t:.8,x:350},{t:1.25,x:390}],'The source document moves along the information-transfer path'),{type:'arrow',x:600,y:385,w:170,color:'#7c8e80'},I(right,850,310,right==='presentation'?260:190,right==='presentation'?208:175,[{t:0,y:355},{t:.75,y:310},{t:1.25,y:295}],'The next document arrives at the output of the information transfer')]});
shots.push(transfer(13.684,15.711,'email','sheet','EMAIL TO SPREADSHEET','Same information.'));
shots.push(transfer(15.711,17.671,'sheet','report','SPREADSHEET TO REPORT','Another rectangle.'));
shots.push(transfer(17.671,20.925458,'report','presentation','REPORT TO PRESENTATION','Explaining the spreadsheet.'));
const project={version:1,style:'B1',width:1280,height:720,fps:30,voice:{path:'preview-narration.wav',lead:0,tail:0},captions,shots,sfx:[{time:.45,kind:'tap',gain:.03},{time:1.0,kind:'chime',gain:.018},{time:5.8,kind:'tap',gain:.025},{time:10.0,kind:'paper',gain:.025},{time:12.2,kind:'paper',gain:.025},{time:14.35,kind:'paper',gain:.022},{time:16.4,kind:'paper',gain:.022},{time:18.4,kind:'paper',gain:.022}],ambience:[{path:'office-bed.wav',start:0,end:20.925458,gain:.07,loop:true,fadeIn:.05,fadeOut:.2}],reference_review:{author_id:'codex-production',capability:{mode:'limited',environment:'Codex desktop, upstream B1 manifest renderer, original SVG-derived layered art, macOS Samantha',limitations:[{capability:'narration',observed:'User selected the installed macOS voice for the pace preview.',impact:'Temporary OS voice; not the Gemini sample voice.'},{capability:'reference playback/listening',observed:'Reference stills inspected; normal-speed audible baseline comparison not performed.',impact:'No sample-equivalence or final creative acceptance claimed.'}]}}};
fs.writeFileSync(path.join(base,'project.json'),JSON.stringify(project,null,2));
fs.writeFileSync(path.join(base,'caption-timing.json'),JSON.stringify({method:'Observed silencedetect boundaries at -36dB, minimum pause .09s, on actual continuous macOS recording; word-level refinement pending for long cues.',captions},null,2));
console.log(JSON.stringify({art_assets:19,shots:shots.length,duration:20.925458,project:path.join(base,'project.json')}));
