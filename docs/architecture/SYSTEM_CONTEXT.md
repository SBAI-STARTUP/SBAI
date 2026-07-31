# SBAI System Context

Version: 1.0.0

Status: Approved

Owner: Founder

Architecture ID: EA-003

Related Documents:
- EA-000 Enterprise Architecture
- EA-001 Domain Model
- EA-002 Layer Model

---

# Purpose

This document defines the external environment in which SBAI operates.

It identifies the primary actors, external systems, and boundaries between SBAI and the outside world.

---

# Primary Actor

## Founder

The Founder is the only human decision-maker within SBAI during the initial phases of development.

Responsibilities include:

- Enterprise governance
- Strategic planning
- Architecture approval
- Product direction
- Security oversight
- Final decision authority

---

# External Systems

## GitHub

Purpose:

- Source code management
- Version control
- Issue tracking
- Pull requests
- Releases

---

## AI Providers

Examples:

- OpenAI
- Anthropic
- Google
- Future enterprise models

Purpose:

- Reasoning
- Code generation
- Research
- Automation

---

## Cloud Providers

Examples:

- AWS
- Google Cloud
- Azure
- Future private infrastructure

Purpose:

- Compute
- Storage
- Networking
- Deployment

---

## Development Environment

Examples:

- Termux
- Acode
- Git
- GitHub CLI
- Future desktop IDEs

Purpose:

- Engineering
- Documentation
- Testing
- Development

---

## Future Customer Platform

Purpose:

- Customer interaction
- Product delivery
- Support
- Account management

(Currently outside implementation scope.)

---

# Enterprise Boundary

Everything inside the SBAI repository is considered part of the enterprise architecture.

External services communicate through documented interfaces and approved integrations.

---

# Context Principles

- SBAI owns its internal architecture.
- External systems are replaceable.
- Integrations must be modular.
- Security applies to every boundary.
- Enterprise knowledge remains under SBAI control.
