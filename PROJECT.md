# Project packet

## Classification

`plotter-image-animations` is a Published Media Snapshot. It preserves public
rendered evidence; it is not a runnable application or a reproducible media
pipeline.

Verified on 2026-07-31 against the original `main` commit
`348af448e71d53ab94a4aa6b4b6d4ad8b2204057`.

## Verified contents

The repository contains three silent 25-second MP4 exports. All are 1920x1080
H.264 video with a white background, a progressive mark-build animation on the
left, and a plate/contact sheet on the right.

| Export | Frame rate | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Portrait | 30 fps | 8,286,219 | `d0bb5232b30e8e1ecc57ff5229b1e5fd7a5746ce99d8d61da2fee447c4df040f` |
| Bathroom | 25 fps | 3,097,091 | `a7bd0d91aface1ccf123401b1f10a253e24e26fa2b0d34811036c78268ba0676` |
| Fashion | 30 fps | 9,713,253 | `fe4c716b0d7dd629b10a35f9ab874ee78413bcdce91557263f13b97f27c19a24` |

The files are ordinary Git blobs, not Git LFS pointers. Their hashes and sizes
are enforced by the repository contract test.

## Custody and reproducibility boundary

The generating source remains unresolved. A local inventory found no duplicate
originals or project files that could regenerate these exact exports. The
repository also lacks a source-image provenance record and an explicit
publication-rights review.

Until that evidence is recovered:

- preserve the three MP4s byte-for-byte;
- do not claim the exports are reproducible;
- do not infer licenses or publication rights from public Git visibility; and
- record newly recovered source as additive evidence before proposing changes
  to the snapshot.

## Runtime and deployment ownership

There is no runtime. GitHub Pages is absent, the GitHub deployments list is
empty, and the repository owns no Droplet or Pugnet process, container, systemd
unit, DNS name, or public endpoint.

The public GitHub repository itself is the current delivery surface for these
files. A Release or archival publication surface may be considered only after
source provenance and publication rights are resolved.

## Validation

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q tests
```

The test suite checks the documentation contract and the exact published media
bytes. Secret scanning and GitHub Actions provide additional repository gates.

## Next decisions

1. [Issue 1](https://github.com/ReidSurmeier/plotter-image-animations/issues/1):
   locate and identify the generating project, source imagery, and export
   process.
2. [Issue 2](https://github.com/ReidSurmeier/plotter-image-animations/issues/2):
   complete a human publication-rights review for the portrait, bathroom, and
   fashion imagery.
3. [Issue 3](https://github.com/ReidSurmeier/plotter-image-animations/issues/3):
   decide whether GitHub Releases or another durable media surface should
   supplement raw repository delivery after provenance is established.
