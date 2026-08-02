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

Export lineage is partially recovered. A cross-repository SHA-256 inventory
found two byte-identical exports in
[`plotter-line-drawing-svg`](https://github.com/ReidSurmeier/plotter-line-drawing-svg)
at its documented `main` commit
`358a33f91e94658791bdbc3ce0f74a00a7a85b22`:

| Snapshot export | Matching export in `plotter-line-drawing-svg/public_assets/` | SHA-256 |
| --- | --- | --- |
| Portrait | `portrait_markbuild_full_duration_full_contact_25s.mp4` | `d0bb5232b30e8e1ecc57ff5229b1e5fd7a5746ce99d8d61da2fee447c4df040f` |
| Bathroom | `animation_left_contact_right_svg_reveal_25s.mp4` | `a7bd0d91aface1ccf123401b1f10a253e24e26fa2b0d34811036c78268ba0676` |

This establishes exact export custody and a repository relationship. It does
not establish which source images, transforms, dependency state, or run inputs
generated those two files. The fashion export remains unmatched. Therefore the
Generating Source remains unresolved for all three subjects.

Until that evidence is recovered:

- preserve the three MP4s byte-for-byte;
- do not claim the exports are reproducible;
- do not infer broader licenses or source provenance from public Git visibility;
  and
- record newly recovered source as additive evidence before proposing changes
  to the snapshot.

## Publication authorization

On 2026-08-02, the repository owner confirmed that they own or are authorized
to publish the three represented source images and all three current Animation
Exports. Continued public distribution of the unchanged snapshot is therefore
authorized. No attribution requirement, distribution limitation, or takedown
action was identified in that review.
The authorization covers all three current Animation Exports.

This is a human authorization record, not recovered Generating Source. The
Generating Source remains unresolved, the exact underlying image identities
are not inferred here, and this authorization does not extend to replacement
media or a new delivery surface without separate review.

ADR 0002 permits a custody-only relocation when the Git commit and all three
media hashes are verified before and after the move. Relocation does not close
the source-provenance issue or make the exports reproducible.

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
   continue from the recovered portrait/bathroom export lineage to identify
   exact run inputs and source imagery, and locate the unmatched fashion
   export.
2. [Issue 2](https://github.com/ReidSurmeier/plotter-image-animations/issues/2)
   records the completed 2026-08-02 human publication-authorization review.
3. [Issue 3](https://github.com/ReidSurmeier/plotter-image-animations/issues/3):
   decide whether GitHub Releases or another durable media surface should
   supplement raw repository delivery after provenance is established.
