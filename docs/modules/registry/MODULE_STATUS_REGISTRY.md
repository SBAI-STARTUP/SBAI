# SBAI Module Status Registry

## Status Definitions

- **IMPLEMENTED** — functioning implementation exists and is tested.
- **PARTIAL** — implementation exists but important capability is incomplete.
- **SCAFFOLD** — structure/placeholders exist without meaningful implementation.
- **DOCUMENTED** — architecture/documentation exists but implementation is not established.
- **VERIFY** — evidence is insufficient.

| Module | Initial Status | Next Action |
|---|---|---|
| API Gateway | PARTIAL/IMPLEMENTED | Harden and align documentation |
| Identity | SCAFFOLD/PARTIAL | Implement identity boundary |
| Configuration | PARTIAL | Establish shared configuration contract |
| Contracts | PARTIAL | Establish stable cross-service contracts |
| Event Bus | SCAFFOLD | Implement after contracts/config |
| Workflow | SCAFFOLD | Implement after event/task foundations |
| Task | SCAFFOLD/PARTIAL | Implement execution contract |
| Notification | SCAFFOLD | Implement after event/task foundations |
| Logging/Audit | PARTIAL | Productionize and standardize |
| Secrets | SCAFFOLD | Implement secure secret boundary |
| Persistence/Data | SCAFFOLD | Establish storage/migration/lifecycle |
| AI Orchestration | SCAFFOLD | Implement governed orchestration |
| Observability | SCAFFOLD | Metrics/tracing/alerting baseline |
| Infrastructure | SCAFFOLD | Define reproducible runtime/deployment |
| CI/CD | SCAFFOLD | Establish automated quality/release gates |

## Important

This registry is intentionally conservative. It does not infer implementation merely because a directory or documentation file exists.
