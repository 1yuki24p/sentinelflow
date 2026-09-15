def print_http_error(log):
    print("HTTP Error Detected")
    print(f"IP: {log['ip']}")
    print(f"Request: {log['method']} {log['path']}")
    print(f"Status: {log['status']}")
    print()


def print_incident(incident):
    print("Security Incident Detected")
    print(f"Type: {incident.incident_type}")
    print(f"IP: {incident.ip}")
    print(f"Severity: {incident.severity}")

    if "failed_attempts" in incident.details:
        print(f"Failed Attempts: {incident.details['failed_attempts']}")

    if "path" in incident.details:
        print(f"Path: {incident.details['path']}")

    if "matched_pattern" in incident.details:
        print(f"Matched Pattern: {incident.details['matched_pattern']}")

    print()