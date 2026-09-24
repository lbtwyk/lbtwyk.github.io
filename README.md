# Yukun Wang — research portfolio

Bilingual personal website preserving the original pixel-art banner, serif typography, compact layout, and gold-and-cream palette. Four selected project videos extend the existing design. Published at [lbtwyk.github.io](https://lbtwyk.github.io/) using GitHub Pages from the root of `main`.

Static HTML, CSS, and JavaScript; no build step. English is the default. The language control saves the visitor's choice; `?lang=zh` and `?lang=en` provide direct links.

## Local preview

Run `python3 -m http.server 8000` from this repository and open `http://localhost:8000`.

## Media

Four selected simulation films, each 144 frames / 4.8 seconds at 30 fps, H.264, no audio. Playback speeds are labeled. Videos loop when visible, preserve a visitor's pause, and do not autoplay when reduced motion is requested.

`scripts/video-sources.json` records original evidence references, durations, and speed factors. Regenerate from the original workspace using a Python environment with PyAV and Pillow:

```sh
python scripts/prepare_videos.py /path/to/original/workspace
```

The original recordings are unchanged. Recovery belongs to the demonstration collection pipeline; upper/lower model execution clips come from separate September evaluations. Selected success clips are not estimates of reliability. The site records the corresponding full-batch completion counts.

The technical report dated September 23, 2026 takes precedence over older resume stage scores for the UBTECH project. Education and research experience follow the latest resume. No private report, model, dataset, or resume PDF is published here.
