def generate_health_summary(log_result):
    errors = log_result.get("errors", 0)
    warnings = log_result.get("warnings", 0)
    timeouts = log_result.get("timeouts", 0)

    # Determine system status
    if errors == 0 and timeouts == 0:
        status = "Healthy"
    elif errors <= 2 and timeouts <= 1:
        status = "Minor issues"
    else:
        status = "Needs attention"

    # Optional: simple health score (keeps it practical, not overcomplicated)
    score = 100 - (errors * 5 + warnings * 2 + timeouts * 3)
    score = max(0, score)

    return {
        "status": status,
        "details": f"{errors} errors, {warnings} warnings, {timeouts} timeouts",
        "health_score": score
    }
