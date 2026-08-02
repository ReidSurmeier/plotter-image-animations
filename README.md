# Plotter Image Animations

Status: **Published Media Snapshot**

This repository preserves three public MP4 exports from plotter mark-build
image tests. It does not contain the generating source, source images, or a
reproducible export pipeline. Treat the checked-in media as published evidence,
not as build output that can currently be regenerated.

Deployment ownership: none. The repository is not an application, has no
GitHub Pages site, and owns no Droplet or Pugnet service.

## Published media

| File | Bytes | Video | SHA-256 |
| --- | ---: | --- | --- |
| `animations/01-portrait-markbuild-full-contact-25s.mp4` | 8,286,219 | 25 s, 1920x1080, H.264, 30 fps, silent | `d0bb5232b30e8e1ecc57ff5229b1e5fd7a5746ce99d8d61da2fee447c4df040f` |
| `animations/02-bathroom-svg-reveal-25s.mp4` | 3,097,091 | 25 s, 1920x1080, H.264, 25 fps, silent | `a7bd0d91aface1ccf123401b1f10a253e24e26fa2b0d34811036c78268ba0676` |
| `animations/03-fashion-markbuild-full-contact-25s.mp4` | 9,713,253 | 25 s, 1920x1080, H.264, 30 fps, silent | `fe4c716b0d7dd629b10a35f9ab874ee78413bcdce91557263f13b97f27c19a24` |

Each export uses a white 1920x1080 layout: a progressive mark build appears on
the left and a plate/contact sheet appears on the right. The subjects are a
portrait, a bathroom scene, and a fashion image.

The portrait and bathroom files are byte-identical to named exports in
[`plotter-line-drawing-svg`](https://github.com/ReidSurmeier/plotter-line-drawing-svg).
That recovers part of their export lineage, but it does not identify the exact
source images, transforms, or run inputs. The fashion export is still unmatched.
On 2026-08-02, the repository owner confirmed that they own or are authorized
to publish all three current Animation Exports. The Generating Source remains
unresolved despite that publication authorization.

Do not recompress, rename, or replace these files until the Generating Source
has been identified and a replacement is separately reviewed. Byte-level tests
intentionally fail if the published snapshot changes.

## Repository guide

- [PROJECT.md](PROJECT.md) records the verified state, ownership boundary, and
  unresolved custody work.
- [CONTEXT.md](CONTEXT.md) defines the repository's domain language.
- [AGENTS.md](AGENTS.md) gives contributor and validation instructions.
- [`docs/adr/`](docs/adr/) records durable decisions.

## Validate

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q tests
```
