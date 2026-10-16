"""Convert Whisper word-timestamp JSON to Herk format without fabricating timing."""
import argparse, json, math, pathlib
def convert(doc,duration):
    if not math.isfinite(duration) or duration<=0: raise ValueError('Supply actual media duration from ffprobe')
    raw=doc.get('words')
    if raw is None:
        segments=doc.get('segments',[])
        if any(s.get('text','').strip() and not s.get('words') for s in segments):
            raise ValueError('Segment timestamps are insufficient; transcribe with word_timestamps=True')
        raw=[w for s in segments for w in s.get('words',[])]
    if not raw: raise ValueError('No word timestamps')
    words=[];previous=0
    for w in raw:
        if w.get('type','word')!='word': continue
        text=w.get('word',w.get('text','')).strip()
        start,end=float(w['start']),float(w['end'])
        if not text or not all(map(math.isfinite,[start,end])) or not 0<=start<=end<=duration or start<previous:
            raise ValueError('Invalid or unordered word timestamps; review source transcript')
        previous=end
        words.append({'text':text,'start':start,'end':end,'type':'word'})
    if not words: raise ValueError('No speech words')
    return {'language_code':doc.get('language',doc.get('language_code','und')),'audio_duration_secs':duration,'text':' '.join(w['text'] for w in words),'words':words}
def main():
    p=argparse.ArgumentParser();p.add_argument('source',type=pathlib.Path);p.add_argument('output',type=pathlib.Path);p.add_argument('--duration',type=float,required=True);a=p.parse_args()
    result=convert(json.loads(a.source.read_text(encoding='utf-8-sig')),a.duration)
    with a.output.open('x',encoding='utf-8') as f: json.dump(result,f,ensure_ascii=False,indent=2)
    print(f'Wrote {len(result["words"])} verified timestamp records; ASR wording still needs review.')
if __name__=='__main__':main()
