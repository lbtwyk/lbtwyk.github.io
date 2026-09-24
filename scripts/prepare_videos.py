"""Export website clips without modifying the underlying recordings."""
import argparse
import json
from fractions import Fraction
from pathlib import Path
import av

parser = argparse.ArgumentParser()
parser.add_argument('workspace', type=Path)
parser.add_argument('--only', nargs='+', choices=['planning', 'recovery', 'upper', 'lower'])
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
specs = {
    'planning': {
        'source': 'docs/briefs/handlingbox-data-collection-brief-20260722/videos/transfer_lower_level.mp4',
        'category': 'collection', 'segments': None, 'poster_frame': 100,
    },
    'recovery': {
        'source': 'syntheticdatageneration/logs/cross_level_boundary_recovery_20260811/r04d_lower_place_complete_video/20260811_072505/interventions/attempt-000/recovery-01/combined.mp4',
        'category': 'collection',
        'segments': [[2.5, 7.5, 30], [7.5, 16.0, 30], [16.0, 43.0, 48], [43.0, 50.5, 27]],
        'poster_frame': 20,
        'cut_reason': 'Show shelf-edge contact, loaded retreat, replanned insertion, release; exclude post-success tail.',
        'evidence': 'docs/experiments/EXP-20260811-utars-sdg-cross-level-boundary-recovery.md; r04d metadata: lower_insert_box_shelf_collision, outcome=success, recovery_accepted=true',
    },
    'upper': {
        'source': 'docs/briefs/utars-techreport-20260922/media/上层_新评测/成功_2026080501.mp4',
        'category': 'inference', 'segments': [[0.0, 8.6, 135]], 'poster_frame': 55,
        'cut_reason': 'End after placement and visible hand withdrawal, before repeated post-task arm motion.',
    },
    'lower': {
        'source': 'docs/briefs/utars-techreport-20260922/media/下层/成功_2026080507.mp4',
        'category': 'inference', 'segments': [[0.0, 49.6, 135]], 'poster_frame': 65,
        'cut_reason': 'End with the box released on the lower shelf and hands withdrawn; remove later free motion.',
    },
}
manifest = []
for name, spec in specs.items():
    source = av.open(str(args.workspace / spec['source']))
    stream = source.streams.video[0]
    duration = float(stream.duration * stream.time_base)
    final_source_frame = duration - 1 / float(stream.average_rate)
    segments = spec['segments'] or [[0.0, final_source_frame, 144]]
    targets = []
    for start, end, count in segments:
        assert 0 <= start < end <= duration
        targets.extend(start + (end - start) * i / (count - 1) for i in range(count))
    moving_frames = len(targets)
    targets.extend([targets[-1]] * (144 - moving_frames))
    assert len(targets) == 144
    entry = dict(spec, id=name, source_seconds=round(duration, 4), segments=segments,
                 source_start_seconds=targets[0], source_end_seconds=targets[-1],
                 end_hold_seconds=(144-moving_frames)/30, output_seconds=4.8,
                 frames=144, simulation=True)
    manifest.append(entry)
    if args.only and name not in args.only:
        source.close()
        continue
    output = av.open(str(root / 'assets/videos' / (name + '.mp4')), 'w', options={'movflags': '+faststart'})
    encoder = output.add_stream('libx264', rate=30)
    encoder.width = min(stream.width, 1280) // 2 * 2
    encoder.height = round(stream.height * encoder.width / stream.width / 2) * 2
    encoder.pix_fmt = 'yuv420p'
    encoder.options = {'crf': '22', 'preset': 'medium'}
    index = 0
    def emit(frame, i):
        converted = frame.reformat(width=encoder.width, height=encoder.height, format='yuv420p')
        converted.pts = i
        converted.time_base = Fraction(1, 30)
        for packet in encoder.encode(converted):
            output.mux(packet)
        if i == spec['poster_frame']:
            converted.to_image().save(root / 'assets/posters' / (name + '.jpg'), quality=90)
    for frame in source.decode(stream):
        time = float(frame.time or 0)
        while index < 144 and time + .0001 >= targets[index]:
            emit(frame, index)
            index += 1
        if index == 144:
            break
    assert index == 144, f'{name}: source ended before cut endpoint'
    for packet in encoder.encode():
        output.mux(packet)
    output.close()
    source.close()
    print(f'{name}: source {targets[0]:.2f}–{targets[-1]:.2f}s -> 4.8s', flush=True)
(root / 'scripts/video-sources.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
