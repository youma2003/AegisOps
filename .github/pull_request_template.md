## What
<!-- One or two sentences. Link the issue: Closes #12 -->

## Scope
- [ ] probe  - [ ] telemetry  - [ ] shield  - [ ] engine  - [ ] commander  - [ ] proto/events  - [ ] deploy  - [ ] docs

## Definition of done
- [ ] Layers respected (controller → service → repository), constructor injection
- [ ] Unit tests for new logic; integration test if it touches DB, Kafka or gRPC
- [ ] Logs carry traceId; errors are `application/problem+json`; endpoints secured with the right role
- [ ] Flyway script added for any schema change
- [ ] Contracts (`proto/`, `events/`) unchanged **or** approved by all three members
- [ ] Docs updated if behaviour or configuration changed
- [ ] CI green
