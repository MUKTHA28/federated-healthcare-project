import pandas as pd

# Load dataset
data = pd.read_csv("data/diabetes.csv")

print("Before Cleaning:")
print(data.head())

# Replace 0 values with mean (important)
columns = ['Glucose', 'BloodPressure']

for col in columns:
    data[col] = data[col].replace(0, data[col].mean())

# Rename columns (simplify)
data = data.rename(columns={
    'Glucose': 'glucose',
    'BloodPressure': 'bp',
    'Age': 'age',
    'Outcome': 'diabetes'
})

# Keep only needed columns
data = data[['age', 'glucose', 'bp', 'diabetes']]

print("\nAfter Cleaning:")
print(data.head())

# Save cleaned data
data.to_csv("data/cleaned_data.csv", index=False)

print("\n✅ Cleaned data saved!")