import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
export const root=path.dirname(fileURLToPath(import.meta.url));
const configFile=path.join(root,'local.config.json');
const config=fs.existsSync(configFile)?JSON.parse(fs.readFileSync(configFile,'utf8')):{};
const runtime=path.resolve(root,config.runtime||'runtime');
const herk=path.join(runtime,'herk');
const env={...process.env};
env.HYPERFRAMES_NO_TELEMETRY='1';
env.HYPERFRAMES_NO_UPDATE_CHECK='1';
env.PATH=[path.dirname(process.execPath),config.ffmpegDir,config.npmCli&&path.dirname(path.dirname(path.dirname(config.npmCli))),env.PATH].filter(Boolean).join(path.delimiter);
if(config.browser) env.HYPERFRAMES_BROWSER_PATH=config.browser;
function run(cmd,args,cwd=root){const r=spawnSync(cmd,args,{cwd,env,stdio:'inherit',windowsHide:true});if(r.error)throw r.error;if(r.status!==0)process.exit(r.status||1);}
function npm(args,cwd){
  const candidates=[config.npmCli,...env.PATH.split(path.delimiter).map(p=>path.join(p,'node_modules/npm/bin/npm-cli.js'))].filter(Boolean);
  const cli=candidates.find(p=>fs.existsSync(p));
  if(cli)run(process.execPath,[cli,...args],cwd);
  else if(process.platform!=='win32')run('npm',args,cwd);
  else throw Error('npm not found. Install Node.js LTS with npm, or configure npmCli with its npm-cli.js path.');
}
const [action,...args]=process.argv.slice(2);
switch(action){
case 'configure': {
  const next={...config};
  for(let i=0;i<args.length;i+=2){if(!['ffmpegDir','npmCli','browser','runtime'].includes(args[i])||!args[i+1])throw Error('Expected key value pairs: ffmpegDir npmCli browser runtime');next[args[i]]=args[i+1];}
  fs.writeFileSync(configFile,JSON.stringify(next,null,2)+'\n');console.log('Saved local configuration (not included in portable ZIP).');break;
}
case 'doctor':
  console.log('Node',process.version,'; requires >=22');
  if(Number(process.versions.node.split('.')[0])<22)process.exitCode=1;
  for(const [cmd,a] of [['ffmpeg',['-version']],['ffprobe',['-version']]]){
    const r=spawnSync(cmd,a,{env,encoding:'utf8',windowsHide:true});console.log(cmd,r.error?.message||(r.stdout||r.stderr).split(/\r?\n/)[0]);if(r.error||r.status!==0)process.exitCode=1;
  }
  console.log('Herk runtime:',fs.existsSync(path.join(herk,'node_modules/hyperframes/package.json'))?'installed':'not installed');
  console.log('Browser override:',config.browser?fs.existsSync(config.browser):'auto-discovery');break;
case 'setup':
  if(!fs.existsSync(herk)){fs.mkdirSync(runtime,{recursive:true});fs.cpSync(path.join(root,'vendor/herk'),herk,{recursive:true,errorOnExist:true});}
  npm(['ci','--no-fund','--no-audit'],herk);
  run(process.execPath,['scripts/setup.mjs'],herk);break;
case 'setup-remotion': {
  const dest=path.join(runtime,'remotion');
  if(!fs.existsSync(dest))fs.cpSync(path.join(root,'templates/remotion'),dest,{recursive:true,errorOnExist:true});
  npm(['ci','--no-fund','--no-audit'],dest);break;
}
case 'remotion': {
  const dest=path.join(runtime,'remotion');
  const more=config.browser&&['render','still'].includes(args[0])?['--browser-executable',config.browser]:[];
  run(process.execPath,['node_modules/@remotion/cli/remotion-cli.js',...args,...more],dest);break;
}
case 'herk': run(process.execPath,args,herk);break;
case 'npm': npm(args,herk);break;
case 'ffmpeg': case 'ffprobe': run(action,args,process.cwd());break;
case 'hyperframes': {
  const cliPackage=path.join(herk,'node_modules/hyperframes/package.json');
  const pkg=JSON.parse(fs.readFileSync(cliPackage));
  const bin=typeof pkg.bin==='string'?pkg.bin:pkg.bin.hyperframes;
  run(process.execPath,[path.resolve(path.dirname(cliPackage),bin),...args],process.cwd());break;
}
default: console.log('node kit.mjs configure KEY VALUE | doctor | setup | setup-remotion | remotion ARGS | herk SCRIPT ARGS | npm ARGS | hyperframes ARGS | ffmpeg ARGS | ffprobe ARGS');if(action)process.exitCode=1;
}
