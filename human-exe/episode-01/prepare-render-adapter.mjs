// Project-local scheduling adapter. The installed upstream skill is unchanged.
// Only reference evidence extraction runs concurrently; all source/hash/frame
// checks and unknown review records are retained unchanged.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
const base=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(base,'../../.production-skills/directing-stickman-videos');
const out=path.join(base,'longform/adapter');fs.mkdirSync(out,{recursive:true});
const absolutize=s=>s.replace(/from '(\.\/[^']+)'/g,(_,rel)=>`from ${JSON.stringify(pathToFileURL(path.join(root,'scripts',rel)).href)}`);
let review=fs.readFileSync(path.join(root,'scripts/b-style-reference-review.mjs'),'utf8');
const start=review.indexOf('function extract(source,');
const end=review.indexOf('\nfunction b3ReviewTemplate',start);
if(start<0||end<0)throw Error('Unexpected upstream evidence module');
let helper=review.slice(start,end).replace('function extract(', 'async function extractConcurrent(').replaceAll('command(ffmpeg,','await asyncCommand(ffmpeg,');
const concurrent=`
import {spawn as spawnAsync} from 'node:child_process';
function asyncCommand(exe,args,max=128*1024*1024){return new Promise((resolve,reject)=>{const c=spawnAsync(exe,args,{stdio:['ignore','pipe','pipe']}),chunks=[];let size=0,err='';c.stdout.on('data',b=>{size+=b.length;if(size>max){c.kill();reject(Error('Evidence output too large'));}else chunks.push(b);});c.stderr.on('data',b=>{err=(err+b).slice(-5000);});c.on('error',reject);c.on('close',code=>code===0?resolve(Buffer.concat(chunks)):reject(Error('Evidence extraction failed: '+err)));});}
async function boundedMap(items,limit,fn){const results=new Array(items.length);let cursor=0;await Promise.all(Array.from({length:limit},async()=>{while(cursor<items.length){const i=cursor++;results[i]=await fn(items[i]);}}));return results;}
`;
const old="for(const a of descriptors(plan,timing))artifacts.push({...a,sha256:extract(source,a,plan,ffmpeg,path.join(out,a.file))});";
if(!review.includes(old))throw Error('Unexpected upstream extraction loop');
review=review.replace(old,"artifacts.push(...await boundedMap(descriptors(plan,timing),4,async a=>({...a,sha256:await extractConcurrent(source,a,plan,ffmpeg,path.join(out,a.file))})));" );
review=review.replace("const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');",`const ROOT = ${JSON.stringify(root)};`);
review=absolutize(review)+'\n'+concurrent+'\n'+helper;
fs.writeFileSync(path.join(out,'parallel-reference-review.mjs'),review);
let render=fs.readFileSync(path.join(root,'scripts/autopilot-render.mjs'),'utf8');
render=absolutize(render);
render=render.replace(JSON.stringify(pathToFileURL(path.join(root,'scripts/b-style-reference-review.mjs')).href),JSON.stringify(pathToFileURL(path.join(out,'parallel-reference-review.mjs')).href));
// Bare dependencies resolve from the installed runtime without duplicating them.
render=render.replace("from '@napi-rs/canvas'",`from ${JSON.stringify(pathToFileURL(path.join(root,'node_modules/@napi-rs/canvas/index.js')).href)}`);
fs.writeFileSync(path.join(out,'candidate-renderer.mjs'),render);
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
fs.writeFileSync(path.join(out,'adapter-manifest.json'),JSON.stringify({scope:'Only scheduling of actual evidence extraction, four concurrent jobs. No approval/acceptance checks removed or filled.',upstream_renderer_sha256:sha(fs.readFileSync(path.join(root,'scripts/autopilot-render.mjs'))),local_renderer_sha256:sha(render),local_reference_module_sha256:sha(review)},null,2));
console.log(out);
