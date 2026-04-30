# AI System Analysis Tools

A practicle project to analyze system logs, generate health summaries, and detect anomalies — with a focus on keeping things simple and practical.

---

## Why I’m Building This

With experience in cloud systems and incident debugging, I’ve spent time understanding how systems fail.

This project is where that meets my interest in AI — especially how we can evaluate system behavior and responses.

---

## What It Does

* Parses logs (errors, warnings, timeouts)
* Generates a system health summary
* Detects basic anomalies

---

## How It Runs

```id="y9s3wd"
Logs → Analyzer → Summary → Anomaly Detection
```

* Runs locally with Python
* Dockerized for consistency
* Includes a simple CI pipeline (GitHub Actions + pytest)

---

## Run Locally

```bash id="k9x2pl"
python3 main.py
```

---

## Run with Docker

```bash id="l0w8rt"
docker build -t ai-system-analysis-tool .
docker run ai-system-analysis-tool
```

---

## Example Output

```id="v8m1qz"
Log Analysis Result:
{'errors': 1, 'warnings': 1, 'timeouts': 1}

System Summary:
{'status': 'Minor issues', 'details': '1 errors, 1 warnings, 1 timeouts', 'health_score': 90}

Anomaly Detection:
{'status': 'No major anomalies', 'details': 'System behavior looks normal'}
```

---

## Next Steps

* Improve anomaly detection
* Explore AI-based evaluation
* Work with more realistic log data

