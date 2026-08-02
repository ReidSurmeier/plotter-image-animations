# ADR 0002: Accept owner publication authorization

- Status: Accepted
- Date: 2026-08-02

## Context

The repository already distributes three immutable Animation Exports. Public
visibility alone did not establish Publication Rights, so issue 2 required a
human review before relocation or any expansion of delivery.

On 2026-08-02, the repository owner confirmed that they own or are authorized
to publish the portrait, bathroom, and fashion images represented in all three
current Animation Exports. No attribution requirement, distribution
limitation, or takedown action was identified in that review.

The review did not recover the exact source-image identities, run inputs, or
project state. The Generating Source remains unresolved for all three exports.

## Decision

Accept the owner's attestation as authorization for continued public
distribution of the unchanged three-file Published Media Snapshot.

This decision does not authorize replacement media, recompression, renaming,
or a new publication surface. Those actions still require recovered source
evidence and separate review.

A custody-only relocation of the repository is allowed when it:

- preserves the Git commit and working-tree cleanliness;
- verifies all three recorded sizes and SHA-256 hashes before and after the
  move; and
- retains the open source-provenance issue without claiming reproducibility.

## Consequences

Publication authorization no longer blocks an unchanged repository move. The
source-provenance work remains open and visible. A successful move proves
custody continuity only; it does not prove Generating Source or grant a broader
license.
