import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load clustered data
df = pd.read_csv('/workspaces/Flipkart-GRiD-6.0/flipkart_ai_size_chart/dataset/clustered_data.csv')

# Clean and preprocess the data
df = df.iloc[1:]  # Skip the header row
df.columns = ['Cluster', 'Weight_mean', 'Weight_std', 'Bust_Chest_mean', 'Bust_Chest_std', 'Waist_mean', 'Waist_std', 'Hips_mean', 'Hips_std']

# Extract features and target
X = df.drop(columns=['Cluster'])
y = df['Cluster']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and feature names
joblib.dump(model, '/workspaces/Flipkart-GRiD-6.0/flipkart_ai_size_chart/models/size_prediction_model.pkl')
feature_names = X.columns.tolist()
joblib.dump(feature_names, '/workspaces/Flipkart-GRiD-6.0/flipkart_ai_size_chart/models/feature_names.pkl')

# Make predictions and get confidence scores
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)
confidence_scores = y_prob[range(len(y_test)), y_pred]

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Print average confidence score
avg_confidence = confidence_scores.mean()
print(f"Average Confidence Score: {avg_confidence:.2f}")
