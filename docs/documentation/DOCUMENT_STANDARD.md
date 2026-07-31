# SBAI Document Standard

Version: 1.0.0

Status: Approved

Owner: Founder

Document ID: DOC-001

---

# Purpose

This standard defines the required structure, metadata, lifecycle, and governance for all documentation within the SBAI repository.

---

# Mandatory Metadata

Every document shall contain:

- Title
- Document ID
- Version
- Status
- Owner
- Created Date
- Last Updated
- Related Modules

---

# Document Status

- Draft
- Review
- Approved
- Frozen
- Deprecated

---

# Versioning

Major.Minor.Patch

Examples:

1.0.0
1.1.0
2.0.0

---

# File Naming

Use uppercase with underscores for standards and constitutional documents.

Examples:

DOCUMENT_STANDARD.md
MODULE_STANDARD.md
PROJECT_SCOPE.md

Use lowercase only where required by tooling.

Examples:

README.md
LICENSE
.gitignore

---

# Repository Rule

No engineering artifact shall exist without appropriate documentation unless explicitly exempted by an approved ADR.