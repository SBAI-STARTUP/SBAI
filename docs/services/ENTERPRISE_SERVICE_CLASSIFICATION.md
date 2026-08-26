Enterprise Service Classification

Version: 1.0.0
Status: Approved

---

Purpose

This document defines how Enterprise Services are classified across SBAI so that each service has a clear criticality, domain, and security profile.

---

Classification Dimensions

Every service shall be classified along these dimensions:

- Domain
- Criticality
- Security Sensitivity
- Operational Scope
- Dependency Importance
- Lifecycle State

---

Domain Categories

A service belongs to one primary domain:

- Core
- Knowledge
- AI
- Security
- Infrastructure
- Integration
- Operations
- Founder
- Business
- Customer
- Data
- Platform

---

Criticality Levels

Critical

The service is required for enterprise survival or secure operation.

High

The service is required for normal enterprise operation.

Medium

The service supports important but non-core functionality.

Low

The service is useful but not operationally essential.

---

Security Sensitivity Levels

Public

Safe for external visibility.

Internal

Restricted to SBAI internal use.

Confidential

Sensitive enterprise information.

Restricted

High-value or high-risk enterprise information.

Founder Only

Accessible only by the Founder or explicitly authorized mechanisms.

---

Operational Scope

Each service shall define whether it is:

- enterprise-wide
- domain-specific
- platform-specific
- workflow-specific
- AI-specific
- infrastructure-specific

---

Classification Rules

A service must not be implemented without:

- a domain assignment
- a criticality assignment
- a sensitivity assignment
- a dependency assignment
- an owner assignment

---

Example Classification Pattern

- ES-001 Identity Service → Core / Critical / Restricted
- ES-007 Audit Service → Core / Critical / Restricted
- ES-008 Policy Service → Governance / Critical / Restricted
- ES-002 Memory Service → Knowledge / High / Confidential

---

Governance Use

Classification is used for:

- access control
- review frequency
- audit requirements
- retention rules
- deployment restrictions
- dependency planning

---

Related Standards

- Enterprise Service Governance
- Enterprise Service Lifecycle
- Enterprise Service Metadata Standard
- Enterprise Object ID Standard
- Enterprise Data Classification

---

Next

The next service standard is the Enterprise Service Metadata Standard.
