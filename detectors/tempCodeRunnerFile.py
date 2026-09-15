def detect_suspicous_requests(logs):

    incidents = []

    # patterns that you commonly see in path traversal attempts.
    suspicous_patterns = [
         "../",
        "..\\",
        "/etc/passwd"
    ]

    # looking at every HTTP log entry
    for log in logs:

        # Get the requested URL/path
        path = log["path"]

        #Checking whether any suspicous pattern appears in the path
        for pattern in suspicous_patterns:

            if pattern in path:

                incident = {
                    "type": "Path Traversal",
                    "ip": log["ip"],
                    "path": path,
                    "severity": "HIGH"
                }

                incidents.append(incident)

                # stop checking other patterns for this requests
                break

    return incidents
