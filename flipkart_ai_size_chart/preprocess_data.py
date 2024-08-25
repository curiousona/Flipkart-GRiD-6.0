import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('/workspaces/Flipkart-GRiD-6.0/flipkart_ai_size_chart/dataset/body_measurements_dataset.csv')

# Identify numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns

# Handle missing values for numeric columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Handle missing values for non-numeric columns (optional)
# df.fillna('missing', inplace=True)  # Example for filling missing values in non-numeric columns

# Standardize the data
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[numeric_cols]), columns=numeric_cols)

# Save the preprocessed data
df_scaled.to_csv('flipkart_ai_size_chart/dataset/preprocessed_data.csv', index=False)
print("Data preprocessing complete and saved.")
