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
    print(f"Failed Attempts: {incident['failed_attempts']}")
    print(f"Severity: {incident['severity']}")
    print()