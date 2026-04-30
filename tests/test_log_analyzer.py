from log_analyzer import analyze_logs

def test_log_analysis():
    logs = [
        "ERROR: Disk failure",
        "WARNING: High memory",
        "TIMEOUT: Service delay"
    ]

    result = analyze_logs(logs)

    assert result["errors"] == 1
    assert result["warnings"] == 1
    assert result["timeouts"] == 1
