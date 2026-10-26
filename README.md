# Yukun Wang — research portfolio

Bilingual personal website preserving the original pixel-art banner, serif typography, compact layout, and gold-and-cream palette. Four project videos extend the existing design. Published at [lbtwyk.github.io](https://lbtwyk.github.io/) using GitHub Pages from the root of `main`.

Static HTML, CSS, and JavaScript; no build step. English is the default. The language control saves the visitor's choice; `?lang=zh` and `?lang=en` provide direct links.

## Local preview

Run `python3 -m http.server 8000` from this repository and open `http://localhost:8000`.

## Media

Four simulation films, each 144 frames / 4.8 seconds at 30 fps, H.264, no audio. Videos loop when visible, preserve a visitor's pause, and do not autoplay when reduced motion is requested.

`scripts/video-sources.json` records original evidence references, categories, source cut ranges, timing segments, and final-frame holds. Regenerate from the original workspace using a Python environment with PyAV and Pillow:

```sh
python scripts/prepare_videos.py /path/to/original/workspace
```

The original recordings are unchanged. Recovery belongs to the demonstration collection pipeline; upper/lower model execution clips come from separate September evaluations. Full-batch results remain in the original technical report.

The technical report dated September 23, 2026 takes precedence over older resume stage scores for the UBTECH project. Education and research experience follow the latest resume. No private report, model, dataset, or resume PDF is published here.

## Collection and inference

Collection is the fully automated planner/collector: cross-shelf demonstration generation and shelf-edge collision recovery. The recovery film uses the accepted r04d lower-insertion collision trajectory, preserving contact, retreat, replanning, and final release.

Inference is the learned policy making action decisions from observations and a task instruction. The upper and lower films end after release and visible hand withdrawal, before unrelated post-task motion. The upper clip uses successful seed 2026080604 from the latest September 23 upper evaluation, selected for visually balanced left/right movement; it still has pitch during lifting. Source cut endpoints are 8.0 seconds and 49.6 seconds; originals are retained. A short final-frame hold makes the completed placement visible without retaining the subsequent motion. Public labels describe capabilities, not export timing or dataset counts.

## Resume demo sections (2026-10-14)

- `?lang=zh#tsinghua`: two real-robot excerpts from user-supplied `rl-co-introduction.mp4`: 98.000–123.296296 s and 123.296296–143.111111 s. Original task/comparison/speed labels retained; narration removed for standalone playback. H.264 MP4 with fast-start metadata.
- `?lang=zh#ubtech`: existing four simulation demonstrations, unchanged.
- `?lang=zh#foredance`: clearly labelled video placeholder, ready for the user's upcoming demo.
- Checked six videos load in Chrome and mobile layout has no horizontal overflow.

## Copy refresh (2026-10-14)

Bilingual profile, ForeDance, internship introductions, demo captions, keywords, and search/share descriptions align with the current CV. Focus: multimodal motion generation, whole-body control, VLA, and sim-to-real learning. Text/keyframe conditioning remains explicitly planned. Video assets and anchors are unchanged. English and Chinese layouts checked at 1050 px and 390 px without horizontal overflow.

## ForeDance song-switch demo (2026-10-14)

Replaced the ForeDance placeholder with the user-supplied `train_switch_slow_a_seed1234.mp4`: full 60 seconds, 1920×1080, original H.264 video and AAC audio retained without re-encoding. Fast-start container and a poster added. User-initiated playback preserves audio; this video is excluded from viewport autoplay. Existing internship videos are unchanged. Local Chrome playback and 390 px mobile layout verified.

2026-10-15: Replaced the ForeDance clip with user-supplied `foredance-diff展示.mp4`, showing generated reference and SONIC execution side by side. Retained the full 60 seconds and original video/audio streams; refreshed poster and media cache versions.

## aheadance update (2026-10-26)

Public project name is `aheadance`. Chinese and English copy follows the approved CV, with concise streaming generation and whole-body control descriptions, 90.6 ms generation per 0.53 s motion and user-confirmed ~0.8 s real-robot end-to-end latency. Text/keyframe conditioning remains planned. The existing demo is labelled simulation; all media and analytics are retained. `#aheadance` is the current anchor and `#foredance` remains compatible with existing CV links.
