-- Runs once, when the postgres volume is created. One database per service (section 9).
CREATE DATABASE telemetry_db;   -- M1
CREATE DATABASE shield_db;      -- M2
CREATE DATABASE commander_db;   -- M3

-- commander-service stores runbook embeddings with pgvector
\c commander_db
CREATE EXTENSION IF NOT EXISTS vector;
