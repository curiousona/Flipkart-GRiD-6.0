import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load preprocessed data
df = pd.read_csv('flipkart_ai_size_chart/dataset/preprocessed_data.csv')

# Print column names for verification
print("Columns in DataFrame:", df.columns)

# Choose columns for clustering (update according to available columns)
columns_for_clustering = ['Weight', 'Bust/Chest']  # Example columns; adjust as needed

# Ensure the chosen columns exist in the DataFrame
if not all(col in df.columns for col in columns_for_clustering):
    raise ValueError("One or more required columns are missing in the data.")

# Apply KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[columns_for_clustering])

# Save clustered data
df.to_csv('flipkart_ai_size_chart/dataset/clustered_data.csv', index=False)

# Visualize clusters
plt.scatter(df['Weight'], df['Bust/Chest'], c=df['Cluster'])
plt.xlabel('Weight')
plt.ylabel('Bust/Chest')
plt.title('Body Type Clustering')
plt.show()
