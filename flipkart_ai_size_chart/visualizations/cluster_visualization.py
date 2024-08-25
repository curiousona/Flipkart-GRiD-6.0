import pandas as pd
import matplotlib.pyplot as plt

# Load clustered data
df = pd.read_csv('flipkart_ai_size_chart/dataset/clustered_data.csv')

# Visualize clusters
plt.scatter(df['Weight'], df['Bust/Chest'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Weight')
plt.ylabel('Bust/Chest')
plt.title('Body Type Clustering')
plt.colorbar(label='Cluster')
plt.show()
