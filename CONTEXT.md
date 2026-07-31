# Plotter Image Animations context

## Purpose

Preserve the known public animation exports and make their custody,
reproducibility, publication, and deployment boundaries explicit.

## Domain language

### Published Media Snapshot

A fixed set of rendered files preserved as public evidence. A snapshot can be
validated byte-for-byte but is not automatically reproducible.

### Animation Export

One final MP4 in `animations/`. It is an immutable member of the current
Published Media Snapshot.

### Mark-build

The progressive appearance of plotter-like marks in the left panel of each
Animation Export.

### Plate/Contact Sheet

The static right-hand panel showing the component marks or printing plates that
correspond to the animation.

### Generating Source

The project files, source imagery, transforms, scripts, dependencies, and
export settings needed to reproduce an Animation Export. The Generating Source
for this snapshot has not been located.

### Recovered Export Lineage

A byte-identical export found in another documented repository. Recovered
Export Lineage proves custody of an output and a repository relationship; it
does not by itself prove reproducibility or identify the source image, run
inputs, transforms, or dependency state that generated the output.

### Publication Rights

The documented authority to distribute the source imagery and derived
Animation Exports. Public repository visibility is not proof of Publication
Rights.

### Deployment Owner

The repository responsible for an active service, DNS route, Pages site, or
other runtime. This snapshot has no Deployment Owner role because it has no
runtime or deployment.

## Invariants

- The three Animation Exports retain their recorded byte sizes and SHA-256
  hashes.
- Recovered Export Lineage is distinguished from complete Generating Source.
- Missing Generating Source is stated as an unresolved custody fact.
- Publication Rights are reviewed by a human before expanding distribution.
- No runtime, Pages, Droplet, or Pugnet ownership is inferred from the presence
  of public media.

## Decision records

- `docs/adr/0001-treat-mp4s-as-published-media-evidence.md`
