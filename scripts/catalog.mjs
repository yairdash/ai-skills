import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';

export function validate(root) {
 const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
 assert.equal(catalog.schema_version,1,'Unsupported catalog schema');
 assert.ok(['public','private'].includes(catalog.visibility),'Invalid visibility');
 assert.equal(catalog.update_policy,'on-request');
 assert.ok(Array.isArray(catalog.entries),'entries must be an array');
 const ids=new Set(); const hosted=new Set();
 for(const e of catalog.entries){
  for(const key of ['id','name','category','description_he','review_status'])assert.ok(typeof e[key]==='string'&&e[key].trim(),`Missing ${key}`);
  assert.match(e.id,/^[a-z0-9]+(?:-[a-z0-9]+)*$/,'Invalid stable id');
  assert.ok(!ids.has(e.id),`Duplicate id: ${e.id}`);ids.add(e.id);
  assert.ok(['external','hosted'].includes(e.kind),'Invalid kind');
  assert.ok(Array.isArray(e.requirements),'requirements must be an array');
  assert.ok(e.requirements.every(x=>typeof x==='string'),'requirements must be strings');
  assert.ok(e.compatibility&&typeof e.compatibility==='object','Missing compatibility');
  for(const surface of ['desktop','web','mobile'])assert.ok(['untested','assessed','tested','unsupported'].includes(e.compatibility[surface]),`Invalid ${surface} compatibility`);
  assert.ok(['content-reviewed','runtime-tested'].includes(e.review_status),'Invalid review status');
  if(Object.values(e.compatibility).includes('tested')||e.review_status==='runtime-tested')assert.ok(e.test_evidence?.length,'Tested entry requires evidence');
  assert.ok(e.source&&typeof e.source.repository==='string','Missing source');
  assert.match(e.source.repository,/^[\w.-]+\/[\w.-]+$/,'Invalid source repository');
  assert.ok(typeof e.source.path==='string'&&e.source.path&&!e.source.path.startsWith('/')&&!e.source.path.split('/').includes('..'),'Invalid source path');
  assert.ok(e.source.revision===null||/^[a-f0-9]{40}$/.test(e.source.revision),'revision must be null or a full Git SHA');
  const url=new URL(e.source.url);
  assert.equal(url.protocol,'https:');assert.equal(url.hostname,'github.com');
  assert.ok(!url.username&&!url.password&&!url.search&&!url.hash,'Credential-free source URL required');
  assert.ok(url.pathname.startsWith(`/${e.source.repository}/tree/`),'Source URL must identify repository and tree path');
  assert.ok(decodeURIComponent(url.pathname).endsWith('/'+e.source.path),'Source URL and path must agree');
  assert.ok(!url.pathname.split('/').some(p=>p==='..'),'Invalid source URL');
  if(e.kind==='hosted'){
   assert.match(e.path,/^skills\/[a-z0-9]+(?:-[a-z0-9]+)*$/,'Invalid hosted path');
   assert.ok(!hosted.has(e.path),'Duplicate hosted path');hosted.add(e.path);
   const p=path.join(root,e.path);
   assert.ok(!fs.lstatSync(p).isSymbolicLink(),'Hosted folder cannot be a symlink');
   const skill=fs.readFileSync(path.join(p,'SKILL.md'),'utf8');
   assert.match(skill,/^---\r?\n/,'Missing skill frontmatter');
   const fm=skill.split(/^---\s*$/m)[1]??'';
   assert.match(fm,/^name:\s*\S/m,'Missing skill name');assert.match(fm,/^description:\s*\S/m,'Missing description');
   assert.ok(fs.existsSync(path.join(p,'PROVENANCE.json')),'Missing hosted provenance');
  } else assert.ok(!e.path,'External links cannot declare a hosted path');
 }
 if(fs.existsSync(path.join(root,'skills')))for(const item of fs.readdirSync(path.join(root,'skills'),{withFileTypes:true}))if(item.isDirectory())assert.ok(hosted.has(`skills/${item.name}`),`Uncatalogued hosted skill: ${item.name}`);
 return catalog;
}
export function render(catalog){
 const esc=s=>String(s).replaceAll('|','\\|').replaceAll('\n',' ');
 const lines=['# קטלוג סקילס','','הקובץ נוצר מ־catalog.json. קישורים חיצוניים מותקנים ממקורם; תאימות מסומנת כהערכה עד שנבדקה בפועל.',''];
 if(!catalog.entries.length)lines.push('טרם נבחרו סקילס לקטלוג. הוראות ההתקנה מוכנות לשימוש לאחר בחירת האוסף הראשון.');
 for(const category of [...new Set(catalog.entries.map(e=>e.category))]){
  lines.push(`## ${category}`,'','| סקיל | שימוש | מיקום | דרישות | בדיקה |','|---|---|---|---|---|');
  for(const e of catalog.entries.filter(e=>e.category===category))lines.push(`| [${esc(e.name)}](${e.kind==='hosted'?e.path:e.source.url}) | ${esc(e.description_he)} | ${e.kind==='hosted'?'במאגר':'מקור חיצוני'} | ${esc(e.requirements.join('; '))} | ${e.review_status==='runtime-tested'?'נבדק בהפעלה':'סקירת תוכן בלבד'} |`);
  lines.push('');
 }
 return lines.join('\n')+'\n';
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const root=path.resolve(import.meta.dirname,'..');
 const mode=process.argv[2]??'validate';assert.ok(['validate','render'].includes(mode),'Use validate or render');
 const catalog=validate(root);
 if(mode==='render')fs.writeFileSync(path.join(root,'CATALOG.md'),render(catalog));
 console.log(`${mode}: ${catalog.entries.length} entries, ${catalog.visibility}`);
}
