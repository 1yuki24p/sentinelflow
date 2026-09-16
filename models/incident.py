class Incident:
    def __init__(self, incident_type, ip, severity, details=None):
        self.incident_type = incident_type
        self.ip = ip
        self.severity = severity
        self.details = details or {}
        self.risk_score = 0

    def __repr__(self):
        return (
            f"Incident("
            f"incident_type='{self.incident_type}', "
            f"ip='{self.ip}', "
            f"severity='{self.severity}', "
            f"risk_score={self.risk_score}, "
            f"details={self.details}"
            f")"
        )