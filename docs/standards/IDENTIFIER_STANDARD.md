# SBAI Identifier Standard

Version: 1.0.0

Status: Approved

Owner: Founder

Document ID: DOC-002

Related Documents:
- EA-000 Enterprise Architecture
- EA-004 Module Map
- ADR-0001 Adopt Enterprise Architecture v1.0

---

# Purpose

This document defines the unique identifier (ID) system used throughout the SBAI repository.

Every permanent engineering artifact shall have a unique identifier within its namespace.

---

# Identifier Format

PREFIX-NUMBER

Examples:

EA-000
ADR-0001
DOC-001
API-0001

Numbers are zero-padded to maintain consistent sorting.

---

# Reserved Identifier Namespaces

## Enterprise Architecture

EA-0000

Examples:

EA-000
EA-001
EA-002

---

## Architecture Decision Records

ADR-0001

Examples:

ADR-0001
ADR-0002

---

## Documentation

DOC-0001

Examples:

DOC-0001
DOC-0002

---

## Constitutional Modules

MOD-0001

---

## Applications

APP-0001

---

## Services

SRV-0001

---

## APIs

API-0001

---

## AI Agents

AI-0001

---

## AI Workflows

WF-0001

---

## Databases

DB-0001

---

## Security Controls

SEC-0001

---

## Infrastructure

INF-0001

---

## Hardware

HW-0001

---

## Robotics

ROB-0001

---

## Operating System

OS-0001

---

## Space Systems

SPC-0001

---

## Research

RES-0001

---

## Templates

TMP-0001

---

## Test Assets

TEST-0001

---

# Identifier Rules

- Every permanent artifact shall have one identifier.
- Identifiers shall never be reused.
- Deprecated identifiers remain reserved.
- Renaming a document shall not change its identifier.
- Cross-references should use identifiers whenever practical.

---

# Future Expansion

New identifier namespaces may be introduced only through an approved Architecture Decision Record (ADR).

