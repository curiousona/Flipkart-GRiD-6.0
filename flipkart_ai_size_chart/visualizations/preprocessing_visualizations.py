import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df_original = pd.read_csv('flipkart_ai_size_chart/dataset/preprocessed_data.csv')

# Print column names for verification
print("Columns in DataFrame:", df_original.columns)

# Visualize the distribution of each feature

# Weight distribution
plt.figure(figsize=(12, 6))
sns.histplot(df_original['Weight'], kde=True)
plt.title('Weight Distribution')
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.show()

# Bust/Chest distribution
plt.figure(figsize=(12, 6))
sns.histplot(df_original['Bust/Chest'], kde=True)
plt.title('Bust/Chest Distribution')
plt.xlabel('Bust/Chest')
plt.ylabel('Frequency')
plt.show()

# Waist distribution
plt.figure(figsize=(12, 6))
sns.histplot(df_original['Waist'], kde=True)
plt.title('Waist Distribution')
plt.xlabel('Waist')
plt.ylabel('Frequency')
plt.show()

# Hips distribution
plt.figure(figsize=(12, 6))
sns.histplot(df_original['Hips'], kde=True)
plt.title('Hips Distribution')
plt.xlabel('Hips')
plt.ylabel('Frequency')
plt.show()

# Boxplot for detecting outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_original[['Weight', 'Bust/Chest', 'Waist', 'Hips']])
plt.title('Boxplot of Body Measurements')
plt.show()
