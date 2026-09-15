class Incident:
    def __init__(self, incident_type, ip, severity, details=None):
        self.incident_type = incident_type
        self.ip = ip
        self.severity = severity
        self.details = details or {}