from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model and feature names
model = joblib.load('flipkart_ai_size_chart/models/size_prediction_model.pkl')
feature_names = joblib.load('flipkart_ai_size_chart/models/feature_names.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        chest = float(request.form.get('chest'))
        waist = float(request.form.get('waist'))
        hips = float(request.form.get('hips'))
        
        # Placeholder values for additional features
        body_shape_index = float(request.form.get('body_shape_index', 0))  # Use form input or default to 0
        bust_chest = float(request.form.get('bust_chest', 0))              # Use form input or default to 0

        # Create DataFrame for prediction with all required features
        input_data = pd.DataFrame([[weight, chest, waist, hips, body_shape_index]], 
                                  columns=feature_names)
        
        # Print DataFrame to check its contents
        print("Input Data for Prediction:")
        print(input_data)
        
        # Predict
        prediction = model.predict(input_data)[0]
        
        return render_template('result.html', size=prediction)
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)

