# Simple tool to analyze logs and count common issues like errors, warnings, and timeouts

def analyze_logs(logs):
    error_count = 0
    warning_count = 0
    timeout_count = 0

    for log in logs:
        log_lower = log.lower()

        if "error" in log_lower:
            error_count += 1
        if "warn" in log_lower:
            warning_count += 1
        if "timeout" in log_lower:
            timeout_count += 1

    return {
        "errors": error_count,
        "warnings": warning_count,
        "timeouts": timeout_count
    }


if __name__ == "__main__":
    sample_logs = [
        "Error connecting to database",
        "Warning: CPU usage high",
        "Timeout occurred while calling API",
        "Service started successfully"
    ]

    result = analyze_logs(sample_logs)

    print("Log Analysis Result:")
    print(f"Errors: {result['errors']}")
    print(f"Warnings: {result['warnings']}")
    print(f"Timeouts: {result['timeouts']}")
