import random
import subprocess

cpu = random.randint(20, 100)
memory = random.randint(30, 90)
latency = random.randint(10, 80)
errors = random.randint(0, 15)

print("=" * 40)
print("LIVE MONITORING")
print("=" * 40)

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Network Latency: {latency} ms")
print(f"Error Rate: {errors}%")

print("\nGrafana ML")

if cpu > 80:
    print("Anomaly Detected!")
    print("\nRecommendation:")
    print("Rollback Deployment")
    print("\nRunning rollback...\n")

    subprocess.run(["python", "deployment/rollback.py"])

else:
    print("No anomalies detected.")
    print("\nDeployment Healthy")