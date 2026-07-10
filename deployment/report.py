import os

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

report = """
# Deployment Report

## Deployment Status

Successful

## Risk Level

Low

## Monitoring

CPU: 34%

Memory: 48%

Errors: 0

## AI Analysis

No anomalies detected.

## Action Taken

Deployment completed successfully.

## Recommendation

Continue monitoring.
"""

with open("reports/deployment_report.md", "w") as file:
    file.write(report)

print("Deployment report created.")