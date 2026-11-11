# Team conventions

Summary of section 5 of `AegisOps-Contracts-and-Plan.pdf`. Changing a rule here = PR approved by all three.

## Ownership

| Folder | Owner |
|---|---|
| `telemetry-service/`, `aegis-probe/`, `deploy/`, `.github/` | M1 (Spring + Go, CI/CD) |
| `shield-service/`, `shield-engine/`, `deploy/initdb/` | M2 (Spring + Quarkus, Auth/JWT + DB) |
| `commander-service/`, `deploy/grafana/`, `docs/` | M3 (Spring + LangChain4j, observability + docs) |
| `proto/`, `events/`, `aegis-proto/` | **all three** — PR approved by everyone |

## Branches and Git workflow

- `main` is protected: changes arrive only by Pull Request, with 1 review and a green CI.
- Each member has a personal integration branch: `m1-telemetry`, `m2-shield`, `m3-commander`.
- For a task, branch from yours or from `main`: `feat/<scope>-<topic>`, `fix/<scope>-<topic>`.
- Merge into `main` at least **once a week** (integration day). Before opening a PR: `git pull origin main`.

## Commits — Conventional Commits

```
feat(probe): add memory leak chaos
fix(shield): expire blocked IPs after ttl
test(commander): saga compensation order
```

Scopes: `probe`, `telemetry`, `shield`, `engine`, `commander`, `proto`, `events`, `deploy`, `ci`, `docs`.

## Java

- Packages: `io.aegisops.telemetry`, `io.aegisops.shield`, `io.aegisops.commander`, `io.aegisops.engine`;
  generated gRPC: `io.aegisops.proto.v1` (module `aegis-proto`).
- Layers in every Spring service: `api/` (controllers + DTOs) · `service/` · `repository/` · `domain/` (entities) ·
  `grpc/` · `messaging/` (Kafka) · `config/`.
- Constructor injection only.

## REST

- Prefix `/api/v1`, JSON camelCase, ISO-8601 UTC dates, pagination `?page=&size=`.
- Errors: RFC 7807 `application/problem+json` with a `traceId` field.
- IDs: UUID strings; servers also have a readable key (`web-01`, `db-01`).

## Headers / metadata

- Humans: `Authorization: Bearer <JWT>` · Probe: `X-API-Key` · All: `X-Trace-Id`.
- gRPC metadata: `x-trace-id`, `x-internal-token`.

## Kafka

- Topics `aegis.<domain>.<name>`, key = `serverId`, JSON envelope (`events/schemas/envelope.schema.json`).
- Dead letters: `<topic>.dlq` after 3 failures.
- Consumers are idempotent: table `processed_event(event_id)` in each Spring DB.
- Adding a field = OK. Removing / renaming = new `version` + PR approved by all three.

## gRPC

- Never change or reuse a field number; only add fields. `buf breaking` enforces it in CI.

## Database

- One database per service; never read another service's tables.
- Every table: `id UUID PK`, `created_at`, `updated_at`, `version` (`@Version`).
- Schema only through Flyway: `V1__init.sql`, `V2__...`; never edit an applied script.

## Ports

| Unit | Ports |
|---|---|
| telemetry-service | HTTP 8081 · gRPC 9191 |
| shield-service | HTTP 8082 · gRPC 9192 |
| shield-engine | HTTP + gRPC 8083 |
| commander-service | HTTP 8084 |
| aegis-probe | gRPC 50051 · HTTP 2112 |
| postgres · kafka · ollama | 5432 · 9092 (host: 9094) · 11434 |
| prometheus · grafana · nginx | 9090 · 3000 · 80 |

## Secrets

Never in Git. Copy `.env.example` to `.env` (ignored) and fill the `CHANGE_ME` values.
