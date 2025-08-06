import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define folder path
images = "images"

# Load the cleaned dataset
df = pd.read_csv("Cleaned_Telco_Customer_Churn.csv")

# Display first 5 rows
print(df.head())

# Define tenure categories
df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 12, 36, df['tenure'].max()], labels=['0-12 months', '13-36 months', '37+ months'])

# Churn rate by tenure group
churn_by_tenure = df.groupby('tenure_group')['churn'].value_counts(normalize=True).unstack()

# Plot the churn rate by tenure
churn_by_tenure.plot(kind='bar', figsize=(8, 5), stacked=True)
plt.title("Churn Rate by Tenure Group")
plt.xlabel("Tenure Group")
plt.ylabel("Proportion")
plt.legend(title="Churn", labels=["No", "Yes"])
plt.show()
plt.savefig(os.path.join(images, "Churn rate by tenure group.png"))  # Save Image

# Churn rate by Gender
plt.figure(figsize=(6, 4))
sns.countplot(x=df['gender'], hue=df['churn'], palette="coolwarm")
plt.title("Churn Rate by Gender")
plt.show()
plt.savefig(os.path.join(images, "churn rate by gender.png"))  # Save Image

# Churn rate by Senior Citizen status
plt.figure(figsize=(6, 4))
sns.countplot(x=df['seniorcitizen'], hue=df['churn'], palette="coolwarm")
plt.title("Churn Rate by Senior Citizen Status")
plt.xticks([0, 1], ['Not Senior', 'Senior'])
plt.show()
plt.savefig(os.path.join(images, "churn rate by senior citizen status.png"))  # Save Image

# Churn rate by payment method
plt.figure(figsize=(10, 5))
sns.countplot(x=df['paymentmethod'], hue=df['churn'], palette="pastel")
plt.title("Churn Rate by Payment Method")
plt.xticks(rotation=45)
plt.show()
plt.savefig(os.path.join(images, "churn rate by payment method.png"))  # Save Image

# Churn rate by contract type
plt.figure(figsize=(8, 5))
sns.countplot(x=df['contract'], hue=df['churn'], palette="coolwarm")
plt.title("Churn Rate by Contract Type")
plt.show()
plt.savefig(os.path.join(images, "Churn rate by contract type.png"))  # Save Image

df.to_csv("Advanced_Analysis_Results.csv", index=False)
