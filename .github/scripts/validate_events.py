"""Contract test: every example in events/examples must match the envelope schema
and the schema of its payload. Run locally with:  python .github/scripts/validate_events.py
"""
import glob
import json
import sys

import jsonschema

PAYLOAD_SCHEMA = {
    "TelemetryMetricEvent": "telemetry-metric",
    "TrafficSampleEvent": "traffic-sample",
    "ChaosInjectedEvent": "chaos-lifecycle",
    "ChaosStoppedEvent": "chaos-lifecycle",
    "CriticalAnomalyDetectedEvent": "critical-anomaly",
    "IpBlockedEvent": "firewall-command",
    "IpUnblockedEvent": "firewall-command",
    "AutoRemediationCompletedEvent": "remediation-completed",
}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


envelope = load("events/schemas/envelope.schema.json")
errors = 0
for path in sorted(glob.glob("events/examples/*.json")):
    event = load(path)
    try:
        jsonschema.validate(event, envelope)
        schema = load(f"events/schemas/{PAYLOAD_SCHEMA[event['eventType']]}.schema.json")
        jsonschema.validate(event["payload"], schema)
        print(f"OK   {path}")
    except (jsonschema.ValidationError, KeyError) as e:
        errors += 1
        print(f"FAIL {path}: {e}")

sys.exit(1 if errors else 0)
