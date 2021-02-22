# IMPORTS
import os
import joblib
import pickle
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


# Flask Setup
app = Flask(__name__)
model = joblib.load('finalized_model.sav')


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

    
# route for PREDICTIONS
@app.route("/predict", methods=['POST']) 
def predict():
    #return '<h1> ****** LOAN APPROVAL PENDING ****** </h1>' 
    loan_predict = model.predict(pd.DataFrame.from_dict({'Gender': ['Female'],
                                                        'Married': ['No'],
                                                        'Dependents': ['0'],
                                                        'Education': ['Graduate'],
                                                        'Self_Employed': ['No'],
                                                        'ApplicantIncome': [4000],
                                                        'CoapplicantIncome': [0],
                                                        'LoanAmount': [500],
                                                        'Loan_Amount_Term': [360.0],
                                                        'Credit_History': [1.0],
                                                        'Property_Area': ['Urban']}))
    return loan_predict


if __name__ == "__main__":
    app.run()

