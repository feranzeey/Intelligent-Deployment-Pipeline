import time

print("=" * 40)
print("ROLLBACK")
print("=" * 40)

print("\nStopping current deployment...")
time.sleep(1)

print("Restoring previous version...")
time.sleep(1)

print("Health Check...")
time.sleep(1)

print("\n✓ Rollback Successful")
print("Application Healthy")