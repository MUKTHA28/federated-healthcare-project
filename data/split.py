import pandas as pd

# Load cleaned data
data = pd.read_csv("data/cleaned_data.csv")

# Shuffle data
data = data.sample(frac=1).reset_index(drop=True)

# Split into 3 parts
n = len(data)
h1 = data[:n//3]
h2 = data[n//3:2*n//3]
h3 = data[2*n//3:]

# Save files
h1.to_csv("data/hospital1.csv", index=False)
h2.to_csv("data/hospital2.csv", index=False)
h3.to_csv("data/hospital3.csv", index=False)

print("✅ Data split into 3 hospitals!")