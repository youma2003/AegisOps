# Decisions log

One entry per decision or open question. Newest at the bottom.

## D1 — Spring Boot 4.1 instead of 3.x (2026-11-11)

The plan says Spring Boot 3, but Spring Initializr only offers 4.x now. The services use **Spring Boot 4.1.2**
(Java 21). Consequences: starters are renamed (`spring-boot-starter-webmvc`, ...) and gRPC is supported
natively (`spring-boot-starter-grpc-server` / `-client`, Spring gRPC). Check that Resilience4j and LangChain4j
starters you add are Boot-4 compatible.

## D2 — Shared Java stubs module `aegis-proto` (2026-11-11)

Java gRPC stubs are generated once, in `aegis-proto/`, from `proto/`. A Spring service adds `io.aegisops:aegis-proto` as a dependency when it starts using gRPC.
Go stubs will be generated with `buf generate` into `aegis-probe/gen/` and committed (M1, once Go + buf are installed).

## D3 — Kafka host port 9094 (2026-11-11)

Inside docker-compose services use `kafka:9092`; from the host / IDE use `localhost:9094`.

## Open questions for the teacher (week 0)

- [ ] NAF / Nuts: packaging only, or also the Nuts Application Framework APIs?
- [ ] Is Go accepted as M1's niche technology?
- [ ] Is Spring Boot 4 acceptable (see D1)?
