# Implementation Roadmap

Version: 1.0.0

Status: Draft

Owner: Founder

Last Updated: 2026-07-30

Related Modules:
- Implementation Module I-001
- Implementation Module I-002
- Implementation Module I-003
- Implementation Module I-004


## Purpose of the implementation architecture

This document describes the implementation-level roadmap and guiding practices for converting SBAI's constitutional and architectural decisions into working software, systems, and operational artifacts. It captures the relationship between high-level architecture and the practical, ordered steps required to deliver the Founder Platform and subsequent product modules.


## Relationship between Constitutional Architecture and Implementation Architecture

- Constitutional Architecture (docs/constitutional): Defines mission, governance, constraints, and long-lived organizational decisions. It sets the "why" and non-functional constraints (security, privacy, legal, policy).
- Implementation Architecture (this document): Defines the "how" — the practical decomposition, build-order, and implementation practices that respect constitutional constraints. Implementation ADRs should trace back to constitutional requirements when applicable.


## Implementation Philosophy

- Dependency-first: Identify and stabilize foundational dependencies early (datastores, auth, core APIs). Build upwards from stable primitives.
- Minimal viable complexity: Implement the smallest coherent slice that delivers value while remaining extensible.
- Document-as-you-build: Every non-trivial implementation change must be captured in ADRs and README.md for the affected module.
- Iterative delivery and rollback safety: Deliver small increments with clear rollback or migration plans.


## Dependency-first development approach

- Identify core dependencies (database, auth, core services) and treat them as first-class modules.
- Implement integration contracts (API schemas, data contracts) early and use them as the scaffolding for parallel work.
- Use mock-compatible interfaces so higher-level work can progress in parallel while dependencies are hardened.


## Current implementation phase

I-004 — Founder Platform Requirements Specification (In progress)

This phase focuses on capturing functional and non-functional requirements for the Founder Platform, defining success criteria, and enumerating required modules and interfaces for the initial implementation iteration.


## Build order

1. I-004 — Founder Platform Requirements Specification (complete requirements and acceptance criteria)
2. I-005 — Founder Platform System Design (architecture & interfaces)
3. I-006 — Database Architecture (schema, migrations, retention, backups)
4. I-007 — API Architecture (contracts, versioning, gateway)
5. I-008 — Authentication (identity, secrets, roles)
6. I-009 — Founder Dashboard (UI + API integration)
7. I-010 — AI Gateway (model orchestration, inference routing)

Note: The build order prioritizes dependency stabilization and testability. Some workstreams (e.g., UI prototypes, research spikes) may run in parallel with core infra development using mocks and feature flags.


## Long-term implementation strategy

- Use ADRs to record key decisions and rationale.
- Keep interfaces stable and migrate with versioned APIs when necessary.
- Automate tests and reproducible builds; introduce CI/CD workflows only when they reduce developer friction and support safe delivery.
- Regularly revisit and update the roadmap as modules are completed or as external constraints change.

