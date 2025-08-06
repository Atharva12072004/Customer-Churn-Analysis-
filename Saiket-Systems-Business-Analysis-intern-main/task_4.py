import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import os

# Define folder path
images = "images"

# Load the cleaned dataset
df = pd.read_csv("Cleaned_Telco_Customer_Churn.csv")

"""We divide tenure into three groups:
  0-12 months → New Customers
  13-36 months → Mid-term Customers
  37+ months → Long-term Customers"""

# Define tenure categories
df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 12, 36, df['tenure'].max()], labels=['0-12 months', '13-36 months', '37+ months'])

# Check the distribution
print(df['tenure_group'].value_counts())

# Pie chart for customer tenure distribution
fig = px.pie(df, names='tenure_group', title='Customer Distribution by Tenure', hole=0.3)  # Donut chart (hole=0.3)
fig.show()

# Group data by tenure and calculate average monthly charges
tenure_charges = df.groupby('tenure_group')['monthlycharges'].mean().reset_index()

# Create a bar chart
fig = go.Figure([go.Bar(x=tenure_charges['tenure_group'], y=tenure_charges['monthlycharges'], text=tenure_charges['monthlycharges'], textposition='auto')])

# Add title and labels
fig.update_layout(title='Average Monthly Charges by Tenure Group', xaxis_title='Tenure Group', yaxis_title='Average Monthly Charges')

fig.show()

# Save Pie Chart
plt.savefig(os.path.join(images, "pie chart for customer tenure distribution.png"))  # Save Image

# Save Bar Chart
plt.savefig(os.path.join(images, "bar chart for average monthlly charges of tenure group.png"))  # Save Image


