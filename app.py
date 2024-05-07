from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the saved Linear Regression model
model = joblib.load(r'C:\Users\HP\OneDrive\Desktop\python\espn\linear_regression_average_predictor.pkl')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input from the form
        Mat = int(request.form['Mat'])
        NO = int(request.form['NO'])
        Runs = int(request.form['Runs'])
        BF = int(request.form['BF'])
        SR = float(request.form['SR'])
        HS = int(request.form['HS'])
        Centuries = int(request.form['100s'])
        Fifties = int(request.form['50s'])

        # Create a DataFrame with user input values
        user_data = pd.DataFrame([[Mat, NO, Runs, BF, SR, HS, Centuries, Fifties]], columns=[
                                 'Mat', 'NO', 'Runs', 'BF', 'SR', 'HS', '100s', '50s'])

        # Make prediction using the loaded model
        user_prediction = model.predict(user_data)

        return render_template('index.html', prediction=user_prediction[0])


if __name__ == '__main__':
    app.run(debug=True)
