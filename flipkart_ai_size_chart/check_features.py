import pandas as pd
import joblib

# Paths to the files
feature_names_path = 'models/feature_names.pkl'
dataset_path = 'dataset/clustered_data.csv'

# Load feature names
feature_names = joblib.load(feature_names_path)
print("Feature Names from file:", feature_names)

# Load dataset
df = pd.read_csv(dataset_path)
print("Columns in dataset:", df.columns.tolist())
