def print_http_error(log):

    print("HTTP Error Detected")
    print(f"IP: {log['ip']}")
    print(f"Request: {log['method']} {log['path']}")
    print(f"Status: {log['status']}")
    print()


def print_incident(incident):

    print("Security Incident Detected")
    print(f"Type: {incident['type']}")
    print(f"IP: {incident['ip']}")

    # Some incidents have failed_attempts.
    # For example, brute-force attacks.
    if "failed_attempts" in incident:
        print(f"Failed Attempts: {incident['failed_attempts']}")

    # Some incidents have a path.
    # For example, path traversal.
    if "path" in incident:
        print(f"Path: {incident['path']}")

    print(f"Severity: {incident['severity']}")
    print()