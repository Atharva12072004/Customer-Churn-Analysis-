import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define folder path
images = "images"

# Load the cleaned dataset
df = pd.read_csv("Cleaned_Telco_Customer_Churn.csv")

# Display basic info
print(df.info())

# Display first 5 rows
print(df.head())

# Summary statistics for numerical columns
print("Summary Statistics:")
print(df.describe())

# Plot histograms for numerical columns
df.hist(figsize=(12, 8), bins=30)
plt.suptitle("Distribution of Numerical Columns", fontsize=16)
plt.savefig(os.path.join(images, "Distribution of numerical column.png"))  # Save Image
plt.show()


# Box plot for Monthly Charges
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['monthlycharges'])
plt.title("Box Plot of Monthly Charges")
plt.savefig(os.path.join(images, "Box plot of mothly charges.png"))  # Save Image
plt.show()

# Count plot for Churn
plt.figure(figsize=(6, 4))
sns.countplot(x=df['churn'], hue=df['churn'], palette="pastel", legend=False)
plt.title("Churn vs Non-Churn Count")
plt.savefig(os.path.join(images, "Churn vs non churn count.png"))  # Save Image
plt.xlabel("Churn")
plt.ylabel("Count")
plt.show()

# Scatter plot of Tenure vs Monthly Charges
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['tenure'], y=df['monthlycharges'], hue=df['churn'])
plt.title("Tenure vs Monthly Charges (Colored by Churn)")
plt.savefig(os.path.join(images, "Tenure vs Monthly charges.png"))  # Save Image
plt.show()

# Churn rate by Contract Type
plt.figure(figsize=(8, 5))
sns.countplot(x=df['churn'], hue=df['churn'], palette="pastel", legend=False)
plt.title("Churn Rate by Contract Type")
plt.savefig(os.path.join(images, "churn rate by contract type.png"))  # Save Image
plt.xlabel("Contract Type")
plt.ylabel("Count")
plt.show()

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['number'])

# Generate heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig(os.path.join(images, "Correlation heatmap.png"))  # Save Image
plt.show()


