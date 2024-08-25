import pandas as pd

# Load the dataset
df = pd.read_csv('/workspaces/Flipkart-GRiD-6.0/flipkart_ai_size_chart/dataset/body_measurements_dataset.csv')

# Explore the dataset
print("Dataset Head:\n", df.head())
print("\nDataset Info:\n", df.info())
print("\nMissing Values:\n", df.isnull().sum())
