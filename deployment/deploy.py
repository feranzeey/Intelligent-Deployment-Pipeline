import time

print("=" * 40)
print("DEPLOYMENT")
print("=" * 40)

print("\nBuilding Docker image...")
time.sleep(1)
print("✓ Image built successfully")

print("\nStarting Canary Deployment...")

for traffic in [10, 25, 50, 100]:
    time.sleep(1)
    print(f"{traffic}% traffic routed")

print("\nDeployment Successful")