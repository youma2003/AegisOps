#!/bin/sh
# Creates the AegisOps topics (section 7 of the plan). Format: name:partitions
set -e
BOOTSTRAP=kafka:9092

for spec in \
  aegis.telemetry.metrics:6 \
  aegis.telemetry.traffic:6 \
  aegis.chaos.lifecycle:3 \
  aegis.alerts.critical:3 \
  aegis.firewall.commands:3 \
  aegis.remediation.completed:3
do
  topic=$(echo "$spec" | cut -d: -f1)
  partitions=$(echo "$spec" | cut -d: -f2)
  /opt/kafka/bin/kafka-topics.sh --bootstrap-server "$BOOTSTRAP" --create --if-not-exists \
    --topic "$topic" --partitions "$partitions" --replication-factor 1
done

/opt/kafka/bin/kafka-topics.sh --bootstrap-server "$BOOTSTRAP" --list
