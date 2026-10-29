# Yukun Wang — research portfolio

Bilingual personal research homepage preserving the original pixel-art banner, serif typography, compact layout, and gold-and-cream palette, with news, research, internships and education. Published at [lbtwyk.github.io](https://lbtwyk.github.io/) using GitHub Pages from the root of `main`.

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

## Academic structure (2026-10-29)

Keeps the original pixel-art banner, gold-and-cream palette and demo cards. Adds a News section and an Education section, renames Projects to Research, and rewrites the About, AHEADance and UBTECH introductions as short research questions rather than CV bullets. Degree shown as integrated master's (MEng) / 本硕连读. AHEADance copy does not add the manuscript title or component names (paper under double-anonymous review). All videos, analytics and anchors (`#aheadance`, `#foredance`, `#ubtech`, `#tsinghua`, demo ids) are retained. English and Chinese checked at 1280 px and 390 px with no horizontal overflow; all seven videos load.

## Wide layout (2026-10-29)

Same palette, pixel banner and demo cards, rearranged to cut scrolling: a two-column header (identity and education beside about and news), AHEADance with its video beside the text, and each internship with text on the left and its demos on the right (UBTECH 2×2, Tsinghua side by side). Below 900 px everything stacks in reading order (identity, about, news, education; project text before its video). Checked at 1440, 1024, 820 and 390 px in both languages: no horizontal overflow, all anchors present, all seven videos load.

## Portrait and institution marks (2026-10-29)

- `assets/portrait.jpg` sits beside Education in the hero (moves right under the nameplate on phones), framed with the slate border and pixel offset shadow.
- `assets/logos/` holds the UCL, UBTECH, Tsinghua and ZGCA marks plus the UTars robot picture, cropped from the resume's source files (see `assets/logos/SOURCES.md`). Marks sit on cream chips so dark or purple artwork stays readable on the dark page; photos and marks opt out of the global pixelated image scaling.

## Chinese banner (2026-10-29)

`assets/banner-zh.png` is the Chinese nameplate (王宇堃 · UCL Robotics & AI 本硕连读 · 机器人学习 / 具身智能) on the same frame, dot grid and robot. It is drawn by `make_banner_zh()` in `scripts/generate_assets.py` with macOS's built-in 16 px bitmap font (`NISC18030.ttf`, no antialiasing) so the glyphs stay true pixels; the page shows it in place of `banner.png` when Chinese is selected.
