import pandas as pd
import numpy as np

# Load clustered data
df = pd.read_csv('flipkart_ai_size_chart/dataset/clustered_data.csv')

# Print column names for verification
print("Columns in clustered data:", df.columns)

# Generate size chart with correct column names
size_chart = df.groupby('Cluster').agg({
    'Weight': [np.mean, np.std],        
    'Bust/Chest': [np.mean, np.std],    
    'Waist': [np.mean, np.std],         
    'Hips': [np.mean, np.std]           
})

# Save size chart
size_chart.to_csv('flipkart_ai_size_chart/dataset/size_chart.csv')
print("Size chart generated and saved.")
