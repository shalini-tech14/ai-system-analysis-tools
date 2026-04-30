from log_analyzer import analyze_logs
from health_summary import generate_health_summary
from anomaly_detector import detect_anomalies

def main():
    # Sample logs (we’ll replace this with real input later)
    logs = [
        "ERROR: Disk failure",
        "WARNING: High memory usage",
        "TIMEOUT: Service did not respond"
    ]

    analysis = analyze_logs(logs)
    summary = generate_health_summary(analysis)
    anomalies = detect_anomalies(analysis)

    print("Log Analysis Result:")
    print(analysis)

    print("\nSystem Summary:")
    print(summary)

    print("\nAnomaly Detection:")
    print(anomalies)

if __name__ == "__main__":
    main()
