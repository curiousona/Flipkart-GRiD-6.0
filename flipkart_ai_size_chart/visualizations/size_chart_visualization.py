import pandas as pd
import matplotlib.pyplot as plt

# Load size chart data with proper header skipping
size_chart = pd.read_csv('flipkart_ai_size_chart/dataset/size_chart.csv', skiprows=2)

# Rename columns for clarity
size_chart.columns = ['Cluster', 'Weight_Mean', 'Weight_Std', 'Bust_Chest_Mean', 'Bust_Chest_Std', 'Waist_Mean', 'Waist_Std', 'Hips_Mean', 'Hips_Std']

# Convert numeric columns to float
numeric_columns = ['Weight_Mean', 'Weight_Std', 'Bust_Chest_Mean', 'Bust_Chest_Std', 'Waist_Mean', 'Waist_Std', 'Hips_Mean', 'Hips_Std']
for col in numeric_columns:
    size_chart[col] = pd.to_numeric(size_chart[col], errors='coerce')

# Check for NaN values after conversion
print("NaN values in DataFrame after conversion:")
print(size_chart.isna().sum())

# Fill NaN values with zero for the purpose of plotting (or choose another method if appropriate)
size_chart.fillna(0, inplace=True)

# Plot size chart
size_chart.set_index('Cluster')[['Weight_Mean', 'Bust_Chest_Mean', 'Waist_Mean', 'Hips_Mean']].plot(kind='bar', figsize=(12, 6))
plt.title('Size Chart by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Measurement')
plt.legend(title='Measurement')
plt.xticks(rotation=0)

# Save the plot as an image file
plt.savefig('flipkart_ai_size_chart/visualizations/size_chart_by_cluster.png')
plt.show()
