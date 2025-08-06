import pandas as pd

# Load the dataset (replace 'your_file.csv' with the actual filename)
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

# Convert 'TotalCharges' to numeric (as found in task 1)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Check missing values before handling
print("Missing Values Before Handling:")
print(df.isnull().sum())

# Check dataset shape before removal
print("Dataset shape before removing missing values:", df.shape)

# Remove rows with any missing values
df.dropna(inplace=True)

# Check missing values after removal
print("Missing Values After Removal:")
print(df.isnull().sum())

# Check dataset shape after removal
print("Dataset shape after removing missing values:", df.shape)

# Check for duplicates
print("Number of duplicate rows:", df.duplicated().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Verify duplicates are removed
print("Number of duplicate rows after removal:", df.duplicated().sum())

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Display standardized column names
print("Updated Column Names:")
print(df.columns)

# Save cleaned dataset
df.to_csv("Cleaned_Telco_Customer_Churn.csv", index=False)
