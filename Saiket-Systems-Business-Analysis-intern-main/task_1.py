import pandas as pd

# Load the dataset (replace 'your_file.csv' with the actual filename)
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

# Display the first 10 rows
print("First 10 Rows of the Dataset:")
print(df.head(10))

# Identify the data types of each column
print("Data Types of Each Column:")
print(df.dtypes)

# Check for missing values
print("Missing Values in Each Column:")
print(df.isnull().sum())

# data type of the column 'Total Charges' is detected as object. To fix this: 

# Convert 'Total Charges' to numeric and handle errors
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Check for missing values again
print("\nMissing Values in Each Column (After Fix):")
print(df.isnull().sum())

# Identify the data types after conversion
print("\nData Types of Each Column (After Fix):")
print(df.dtypes)

