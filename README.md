# Flipkart-GRiD-6.0
AI-Powered Size Chart Generator for Apparel Sellers


# AI-Powered Size Chart Generator for Apparel Sellers

## Overview

This project, developed for the Flipkart Grid 6.0 hackathon, provides an AI-powered solution for generating accurate size charts for apparel sellers. It uses machine learning models and user data to recommend clothing sizes and improve fit accuracy.

## Project Components

1. **Data Processing**: Prepares and clusters body measurement data.
2. **Model Training**: Trains a machine learning model to predict appropriate sizes.
3. **Web Interface**: Allows users to input body measurements and receive size recommendations.
4. **Size Chart Generation**: Creates size charts based on the clustered data and user inputs.

## Project Structure

- **`flipkart_ai_size_chart/`**: Main project directory.
  - **`app.py`**: Flask application serving the web interface.
  - **`check_features.py`**: Script to verify consistency between dataset features and model requirements.
  - **`dataset/`**: Directory containing dataset files.
    - `body_measurements_dataset.csv`: Raw body measurements data.
    - `clustered_data.csv`: Data with clustered body types.
    - `preprocessed_data.csv`: Data preprocessed for model training.
    - `purchase_history.csv`: User purchase history data.
    - `size_chart.csv`: Predefined size chart data.
  - **`models/`**: Directory containing trained models and feature names.
    - `feature_names.pkl`: List of feature names used in the model.
    - `size_prediction_model.pkl`: Trained model for size prediction.
  - **`static/`**: Contains static assets like CSS.
    - `flipkart_style.css`: CSS file to style the web interface.
  - **`templates/`**: HTML templates for the web interface.
    - `index.html`: Homepage for user input.
    - `result.html`: Page displaying size recommendations.
  - **`utils/`**: Utility scripts for various functions.
  - **`visualizations/`**: Scripts for generating data visualizations.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/flipkart-ai-size-chart.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd flipkart-ai-size-chart
   ```

3. **Install required Python packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Flask application**:

   ```bash
   python flipkart_ai_size_chart/app.py
   ```

2. **Open your web browser** and go to `http://127.0.0.1:5000`.

3. **Input body measurements** on the homepage to receive size recommendations.

## Development

### Adding New Features

1. **Update Dataset**: Add or modify files in the `dataset/` directory.
2. **Retrain Model**: Update and retrain the model using the new dataset. Save the updated model in the `models/` directory.
3. **Modify Web Interface**: Update HTML templates and CSS in the `templates/` and `static/` directories respectively.

### Testing

- To check if feature names match between the dataset and the model, run:

  ```bash
  python flipkart_ai_size_chart/check_features.py
  ```


## Acknowledgments

- **Flipkart Grid 6.0 Hackathon**: For providing the opportunity to develop this solution.
- **Libraries and Tools**: Various Python libraries used in this project.

