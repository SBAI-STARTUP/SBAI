# Enterprise Event Standard

Version: 1.0

Status: Approved

---

Every enterprise event contains:

- Event ID
- Event Type
- Timestamp (UTC)
- Source
- Target
- Correlation ID
- Workflow ID
- Identity ID
- Resource ID
- Severity
- Payload
- Signature
- Version

---

Event Naming

DOMAIN.ACTION.RESULT

Examples:

IDENTITY.LOGIN.SUCCESS

IDENTITY.LOGIN.FAILURE

AI.TASK.STARTED

AI.TASK.COMPLETED

WORKFLOW.CREATED

WORKFLOW.FAILED

MEMORY.UPDATED

KNOWLEDGE.NODE.CREATED

SECURITY.THREAT.DETECTED
