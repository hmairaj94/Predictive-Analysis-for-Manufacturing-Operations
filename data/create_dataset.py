import pandas as pd
import random

# Generate synthetic data
n_samples = 500  # Number of rows
data = {
    "Machine_ID": [f"M-{random.randint(1, 20)}" for _ in range(n_samples)],  # Random machine IDs
    "Temperature": [round(random.uniform(50, 100), 2) for _ in range(n_samples)],  # Random temperatures
    "Run_Time": [random.randint(1, 500) for _ in range(n_samples)],  # Random run times (in hours)
    "Downtime_Flag": [random.choice([0, 1]) for _ in range(n_samples)]  # Downtime flag (0 or 1)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("synthetic_machine_data.csv", index=False)

print(df.head())
