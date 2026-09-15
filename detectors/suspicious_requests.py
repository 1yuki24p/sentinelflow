from models.incident import Incident


def suspicious_requests(logs):
    incidents = []

    suspicious_patterns = [
        "../",
        "..\\",
        "/etc/passwd"
    ]

    for log in logs:
        path = log["path"]

        for pattern in suspicious_patterns:
            if pattern in path:
                incident = Incident(
                    incident_type="Path Traversal",
                    ip=log["ip"],
                    severity="HIGH",
                    details={
                        "path": path,
                        "matched_pattern": pattern
                    }
                )

                incidents.append(incident)

                break

    return incidents