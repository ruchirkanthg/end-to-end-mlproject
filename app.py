import os 
import numpy as np
import pandas as pd
from mlproject.pipeline.prediction import PredictionPipeline
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

# Home Page Route - Displays Input Form
@app.route('/')
def home():
    return render_template("index.html")  # Renders the input form page

# Prediction Route - Handles Form Submission and Directly Renders Results
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            # Extract input values from form
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
            # Convert input to NumPy array
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)

            # Use PredictionPipeline to predict wine quality
            predictor = PredictionPipeline()
            predicted_quality = predictor.predict(data)

            # Instead of redirecting, render results.html directly
            return render_template("results.html", quality=str(predicted_quality))

        except Exception as e:
            print(f"Exception Occurred: {e}")
            return render_template('index.html', error="Something went wrong. Please try again.")

# Run Flask Application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)