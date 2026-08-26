# Enterprise Naming Standard (ENS)

Version: 1.0

Status: Approved

---

# Purpose

Provide one naming convention for the entire SBAI ecosystem.

---

# Naming Rules

## Enterprise Objects

PREFIX-NUMBER

Examples

AI-0141

ES-0003

CAP-0140

DOM-0300

WF-000001

TASK-000001

DOC-000001

---

# File Names

PREFIX_DESCRIPTION.md

Examples

ES-003_ENTERPRISE_KNOWLEDGE_GRAPH_SERVICE.md

AI-141_DIRECTOR_OF_OFFENSIVE_SECURITY_AI.md

---

# APIs

/api/v1/resource/action

Example

/api/v1/workflow/create

---

# Events

DOMAIN.ACTION.RESULT

Examples

AI.TASK.STARTED

WORKFLOW.CREATED

---

# Environment Variables

SBAI_<SYSTEM>_<NAME>

Example

SBAI_DB_HOST

---

# Git Branches

architecture/

feature/

security/

fix/

release/

---

# Repository Names

SBAI

SBAI-INFRA

SBAI-DOCS

SBAI-HARDWARE

SBAI-ROBOTICS

SBAI-SPACE
