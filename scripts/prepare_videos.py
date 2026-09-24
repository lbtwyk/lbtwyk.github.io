"""Create the four 4.8-second portfolio films from local evidence. Originals remain unchanged."""
import argparse
import json
from fractions import Fraction
from pathlib import Path
import av

parser = argparse.ArgumentParser()
parser.add_argument('workspace', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
sources = {
 'planning': 'docs/briefs/handlingbox-data-collection-brief-20260722/videos/transfer_lower_level.mp4',
 'recovery': 'syntheticdatageneration/logs/autonomous_replanning_recovery_20260810/r131_first_correction_only_recording/20260810_035248/interventions/attempt-000/recovery-01/combined.mp4',
 'upper': 'docs/briefs/utars-techreport-20260922/media/上层_新评测/成功_2026080501.mp4',
 'lower': 'docs/briefs/utars-techreport-20260922/media/下层/成功_2026080507.mp4',
}
manifest = []
for name, relative in sources.items():
 source = av.open(str(args.workspace / relative))
 stream = source.streams.video[0]
 duration = float(stream.duration * stream.time_base)
 last_time = duration - 1 / float(stream.average_rate)
 targets = [last_time * i / 143 for i in range(144)]
 output = av.open(str(root / 'assets/videos' / (name + '.mp4')), 'w', options={'movflags': '+faststart'})
 encoder = output.add_stream('libx264', rate=30)
 encoder.width = min(stream.width, 1280) // 2 * 2
 encoder.height = round(stream.height * encoder.width / stream.width / 2) * 2
 encoder.pix_fmt = 'yuv420p'
 encoder.options = {'crf': '22', 'preset': 'medium'}
 index = 0
 last = None
 def emit(frame, i):
  frame = frame.reformat(width=encoder.width, height=encoder.height, format='yuv420p')
  frame.pts = i
  frame.time_base = Fraction(1, 30)
  for packet in encoder.encode(frame): output.mux(packet)
  if i == (57 if name == 'lower' else 100):
   frame.to_image().save(root / 'assets/posters' / (name + '.jpg'), quality=90)
 for frame in source.decode(stream):
  time = float(frame.time or 0)
  last = frame
  while index < 144 and time + 0.0001 >= targets[index]:
   emit(frame, index)
   index += 1
 while index < 144:
  emit(last, index)
  index += 1
 for packet in encoder.encode(): output.mux(packet)
 output.close()
 source.close()
 entry = {'id': name, 'source': relative, 'source_seconds': round(duration, 4), 'output_seconds': 4.8, 'speed': round(duration / 4.8, 2), 'frames': 144, 'simulation': True, 'selected_example': True}
 manifest.append(entry)
 print(entry, flush=True)
(root / 'scripts/video-sources.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
