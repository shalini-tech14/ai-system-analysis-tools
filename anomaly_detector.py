def detect_anomalies(log_result):
    errors = log_result.get("errors", 0)
    warnings = log_result.get("warnings", 0)
    timeouts = log_result.get("timeouts", 0)

    anomalies = []

    # Simple rules (keep it practical)
    if errors > 5:
        anomalies.append("High number of errors detected")

    if timeouts > 3:
        anomalies.append("Frequent timeouts observed")

    if warnings > 10:
        anomalies.append("Large number of warnings")

    if not anomalies:
        return {
            "status": "No major anomalies",
            "details": "System behavior looks normal"
        }

    return {
        "status": "Anomalies detected",
        "details": anomalies
    }
