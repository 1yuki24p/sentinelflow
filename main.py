from parser import parse_logs
from detectors.brute_force import detect_brute_force
from detectors.suspicious_requests import detect_suspicous_requests
from utils.output import print_http_error, print_incident
from models.incident import Incident

test_incident = Incident(
    incident_type="Test Incident",
    ip="127.0.0.1",
    severity="LOW",
    details={
        "message": "Testing the incident model"
    }
)


print(test_incident.incident_type)
print(test_incident.ip)
print(test_incident.severity)
print(test_incident.details)

print()

# Parse log file
logs = parse_logs("attack.log")

for log in logs:

    if log["status"] >= 400:
        print_http_error(log)


# Detect brute-force attacks
incidents = detect_brute_force(logs)

# Detect suspicious requests 
suspicious_incidents = detect_suspicous_requests(logs)

# Adding suspicious-request incidients to our existing incidents list
incidents.extend(suspicious_incidents)

# Display incidents
for incident in incidents:
    print_incident(incident)

