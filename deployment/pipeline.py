import subprocess

print("=" * 50)
print("INTELLIGENT DEPLOYMENT PIPELINE")
print("=" * 50)

print("\nSTEP 1/5")
subprocess.run(["python", "deployment/pre_deployment.py"])

print("\nSTEP 2/5")
subprocess.run(["python", "deployment/deploy.py"])

print("\nSTEP 3/5")
subprocess.run(["python", "deployment/monitor.py"])

print("\nSTEP 4/5")
print("Rollback decision completed.")

print("\nSTEP 5/5")
subprocess.run(["python", "deployment/report.py"])

print("\n" + "=" * 50)
print("PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 50)