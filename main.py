from parser import parse_logs
from detectors.brute_force import detect_brute_force
from detectors.suspicious_requests import suspicious_requests
from utils.output import print_http_error, print_incident
from models.incident import Incident
from utils.risk import calculate_risk_score
from detectors.scanning import detect_scanning
from incident_manager import save_incident



# Parse log file
logs = parse_logs("attack.log")

for log in logs:

    if log["status"] >= 400:
        print_http_error(log)


# Detect brute-force attacks
incidents = detect_brute_force(logs)

# Detect suspicious requests 
suspicious_incidents = suspicious_requests(logs)

# Adding suspicious-request incidients to our existing incidents list
incidents.extend(suspicious_incidents)

scanning_incidents = detect_scanning(logs)
incidents.extend(scanning_incidents)

# Display incidents
for incident in incidents:
    incident.risk_score = calculate_risk_score(incident)

    save_incident(incident)

    print_incident(incident)

