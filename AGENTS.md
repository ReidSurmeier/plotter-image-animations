# Plotter Image Animations agent guide

This repository is a Published Media Snapshot containing three checked-in MP4
exports. Read `PROJECT.md` and `CONTEXT.md` before making changes.

## Boundaries

- Preserve every checked-in MP4 byte-for-byte unless a reviewed change
  explicitly replaces the published snapshot.
- Do not recompress, rename, regenerate, or remove media without identified
  generating source, provenance, and publication-rights review.
- Do not claim that the exports are reproducible while the source project is
  unresolved.
- Keep credentials, private machine paths, and raw secret-scan findings out of
  committed files.
- Tests must use the Python standard library and repository fixtures. They must
  not publish media, register services, or mutate external systems.

## Commands

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q tests
gitleaks git --no-banner --redact
```

## Validation

Run the complete unit suite and compile the Python tests before claiming the
repository contract works. Verify media size and SHA-256 values rather than
trusting filenames or visual similarity.

## Agent skills

### Issue tracker

Issues and follow-up custody work live in GitHub Issues for
`ReidSurmeier/plotter-image-animations`. See
`docs/agents/issue-tracker.md`.

### Triage labels

Use the five standard Matt Pocock triage roles. See
`docs/agents/triage-labels.md`.

### Domain docs

This is a single-context repository with `CONTEXT.md` at the root and decisions
in `docs/adr/`. See `docs/agents/domain.md`.
