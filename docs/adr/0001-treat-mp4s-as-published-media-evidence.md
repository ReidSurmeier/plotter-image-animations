# ADR 0001: Treat MP4s as published media evidence

- Status: Accepted
- Date: 2026-07-31

## Context

The repository contains three public MP4 exports but no generating project,
source-image provenance, dependency record, or export instructions. The files
can be inspected and verified byte-for-byte, but they cannot currently be
regenerated from repository contents.

Replacing or recompressing them would destroy the only local evidence of the
published outputs. Conversely, describing them as reproducible would overstate
what the repository proves.

## Decision

Treat the three MP4s as an immutable Published Media Snapshot:

- record and test exact byte sizes and SHA-256 hashes;
- preserve them without transformation;
- state that Generating Source and Publication Rights remain unresolved; and
- keep runtime and deployment ownership explicitly set to none.

Recovered source or rights evidence must be added and reviewed before changing
the snapshot or expanding its delivery surface.

## Consequences

The repository has a meaningful validation gate despite having no application
runtime. Accidental binary replacement fails tests. Future contributors can
distinguish published evidence from reproducible source, while follow-up work
remains visible rather than being guessed into the documentation.
