from models.incident import Incident

def detect_scanning(logs, threshold=5):
    paths_by_ip = {} # stores paths seperately for each ip 

    for log in logs:
        ip = log["ip"]
        path = log["path"]

        if ip not in paths_by_ip:
            paths_by_ip[ip] = set() # automatically removes duplicates

        paths_by_ip[ip].add(path)

    incidents = []

    for ip, paths in paths_by_ip.items():
        if len(paths) >= threshold: # an ip must request at least five unique paths before an incident is created.
            incident = Incident(
                incident_type = "Scanning",
                ip = ip,
                severity = "MEDIUM",
                details={
                    "unique_paths": len(paths),
                    "paths": sorted(paths)
                }
            )

            incidents.append(incident)

        return incidents