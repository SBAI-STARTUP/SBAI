# Documentation Standards

Version: 1.0.0

Status: Draft

Owner: Founder

Last Updated: 2026-07-30

Related Modules:
- Documentation
- Implementation


## Purpose

Define the standards for writing, organizing, and maintaining documentation across the SBAI repository. Consistent documentation makes decisions discoverable, reduces onboarding time, and preserves institutional knowledge.


## Markdown Style

- Use CommonMark-compatible Markdown.
- Prefer ATX headings (#) with a single space after the hash: "# Title".
- Keep lines wrapped at 80-100 characters where feasible for readability.
- Use fenced code blocks with language identifiers (```python, ```bash).
- Use relative links for internal documents when possible.


## Naming Conventions

- Filenames: use kebab-case (lowercase with hyphens) for filenames and directories: e.g., `architecture-principles.md`.
- Document IDs: ADRs use numeric prefix: `0001-use-postgres.md`.
- Images and binary assets: store in assets/ or in a subfolder next to the document with `-assets` suffix.


## Heading Hierarchy

- H1 for document title only. Don’t use multiple H1s in the same file.
- H2 for major sections, H3 for subsections, H4 for micro-sections.
- Start with the standard header block (Title, Version, Status, Owner, Last Updated, Related Modules).


## Diagrams

- Prefer vector formats (SVG) for diagrams. Store diagram source files (e.g., .drawio, .mermaid) alongside exported SVG or PNG.
- Use mermaid for simple diagrams where supported by viewers.
- Include a short caption and alt text for accessibility.


## Versioning

- Every document starts at Version 1.0.0.
- Bump the patch version for minor edits, minor for significant changes, major for breaking or removed content.
- Record changes in CHANGELOG.md when the update affects the project-level decisions or processes.


## Status Tags

Use one of the following statuses in the header:
- Draft — under active authoring
- Active — accepted and current
- Deprecated — superseded by another document


## Review and Ownership

- Every document must include an Owner; for now, default to Founder.
- Document authors should add references to related modules.


## Enforcement

- Maintain a `docs/` index and periodically audit documentation for stale content.
- New folders must include a README.md following docs/templates/folder-readme-template.md.


## Examples

- See `docs/architecture/architecture-principles.md` for a sample architecture doc.
