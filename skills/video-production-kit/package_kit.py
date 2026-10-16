"""Package or install only an explicit distributable allowlist. Python 3.10+."""
import argparse, hashlib, json, pathlib, shutil, zipfile
ROOT=pathlib.Path(__file__).resolve().parent
FILES=['SKILL.md','README.he.md','kit.mjs','package_kit.py','normalize_transcript.py','sources.lock.json','VERIFY.md','LICENSE','THIRD_PARTY_NOTICES.md','PROVENANCE.json','.gitignore']
DIRS=['vendor','references','templates']
def payload():
    files=[ROOT/p for p in FILES]
    files += [p for d in DIRS for p in (ROOT/d).rglob('*') if p.is_file()]
    # Newer upstream HyperFrames material is documentation only, not executable
    # skill installs or a license to redistribute its auxiliary media assets.
    docs=ROOT/'references/hyperframes'
    files=[p for p in files if not p.is_relative_to(docs) or p.suffix=='.md' or p.name=='LICENSE']
    for p in files:
        if p.is_symlink() or not p.resolve().is_relative_to(ROOT): raise ValueError('Escaping file')
        if any(x in p.relative_to(ROOT).parts for x in ('node_modules','runtime','.env','.git')): raise ValueError('Runtime data in payload')
        if not p.is_file(): raise ValueError(f'Missing {p.name}')
    return sorted(files)
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--install',type=pathlib.Path,help='Exact NEW skill directory, e.g. PROJECT/.agents/skills/video-production-kit')
    parser.add_argument('--use-local-runtime',action='store_true')
    a=parser.parse_args()
    files=payload()
    manifest={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    if a.install:
        dest=a.install.resolve()
        if dest.exists(): raise SystemExit('Destination already exists; preserving it. Choose a new directory or review a manual upgrade.')
        dest.mkdir(parents=True)
        for p in files:
            target=dest/p.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
        (dest/'package-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
        if a.use_local_runtime:
            config=json.loads((ROOT/'local.config.json').read_text()) if (ROOT/'local.config.json').exists() else {}
            config['runtime']=str((ROOT/config.get('runtime','runtime')).resolve())
            (dest/'local.config.json').write_text(json.dumps(config,indent=2)+'\n')
        print(f'Installed {len(files)} files at {dest}. Available to Codex next turn.')
    else:
        dest=ROOT/'dist/video-production-kit.zip';dest.parent.mkdir(exist_ok=True)
        with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
            for p in files:z.write(p,'video-production-kit/'+p.relative_to(ROOT).as_posix())
            z.writestr('video-production-kit/package-manifest.json',json.dumps(manifest,indent=2)+'\n')
        (dest.parent/'video-production-kit.sha256').write_text(hashlib.sha256(dest.read_bytes()).hexdigest()+'  '+dest.name+'\n')
        print(f'{len(files)} files; {dest.stat().st_size:,} bytes; {dest}')
if __name__=='__main__': main()
