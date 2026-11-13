import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const base=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(base,'../../.production-skills/directing-stickman-videos');
const {loadProject}=await import(path.join(root,'scripts/autopilot-core.mjs'));
const {painter,render}=await import(process.argv.includes('--parallel-evidence')?path.join(base,'longform/adapter/candidate-renderer.mjs'):path.join(root,'scripts/autopilot-render.mjs'));
const p=loadProject(path.join(base,'longform/project.json'));
const dir=path.join(base,'longform/review-stills');fs.mkdirSync(dir,{recursive:true});
if(process.argv.includes('--stills')){
 const require=createRequire(path.join(root,'package.json'));
 const {createCanvas}=require('@napi-rs/canvas');
 const paint=await painter(p);
 const pageSize=12;
 for(let page=0;page<Math.ceil(p.shots.length/pageSize);page++){
  const sheet=createCanvas(1280,600),ctx=sheet.getContext('2d');ctx.fillStyle='#fff';ctx.fillRect(0,0,1280,600);
  for(let j=0;j<pageSize;j++){
   const i=page*pageSize+j;if(i>=p.shots.length)break;const shot=p.shots[i],t=(shot.start+shot.end)/2;
   const frame=paint(t),x=(j%4)*320,y=Math.floor(j/4)*200;
   ctx.drawImage(frame,x,y+20,320,180);ctx.font='12px sans-serif';ctx.fillStyle='#26322a';ctx.fillText(`SHOT ${i+1} / ${t.toFixed(2)}s`,x+5,y+14);
  }
  fs.writeFileSync(path.join(dir,`page-${String(page+1).padStart(2,'0')}.png`),sheet.toBuffer('image/png'));
 }
 console.log(JSON.stringify({pages:Math.ceil(p.shots.length/pageSize),shots:p.shots.length}));
}else{
 // The user explicitly requested the full ten-minute video. Export a complete
 // review candidate, without manufacturing CLI approval or independent review.
 // The renderer's report/evidence remain pending; this is not accept-visual.
 const authorization={request:'làm bản 10 phut đi',scope:'Full approximately ten-minute video using the presented B1 direction and selected Mac voice',independent_reference_acceptance:'not inferred',exact_sample_acceptance:'not fabricated',publishing:'not authorized'};
 fs.writeFileSync(path.join(base,'longform/generation-authorization.json'),JSON.stringify(authorization,null,2));
 const report=await render(p,{full:true,replace:process.argv.includes('--replace')});
 console.log(JSON.stringify({output:report.output,duration:report.duration,full_decode:report.full_decode,frames:report.frames,visual_acceptance:report.visual_acceptance}));
}
