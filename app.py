# IMPORTS
import os
import joblib
import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


# Flask Setup
app = Flask(__name__)
# loaded_model = joblib.load(filename)
# model loading
# filename = 'finalized_model.sav'
# joblib.dump(rf, filename)
filename = 'finalized_model.sav'
# filename = 'balanced_model.sav'
loaded_model = joblib.load(filename)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

    
# route for PREDICTIONS
@app.route("/predict", methods=['GET'])
def predict():
    # li=[]
    i1=request.args.get('Gender')
    i2=request.args.get('Marital')
    i3=request.args.get('Dependents')
    i4=request.args.get('Education')
    i5=request.args.get('Employed')
    i6=request.args.get('Applicant')
    i7=request.args.get('Coapplicant')
    i8=request.args.get('Loan')
    i9=request.args.get('Term')
    i10=request.args.get('Credit')
    i11=request.args.get('Property')
    # li.append(i1)
    # li.append(i2)
    # li.append(i3)
    # li.append(i4)
    # li.append(i5)
    # li.append(i6)
    # li.append(i7)
    # li.append(i8)
    # li.append(i9)
    # li.append(i10)
    # li.append(i11)
    # data = pd.DataFrame.from_dict({'Gender': ['Male'],
    # 'Married': ['Yes'],
    # 'Dependents': ['2'],
    # 'Education': ['Graduate'],
    # 'Self_Employed': ['No'],
    # 'ApplicantIncome': [3100],
    # 'CoapplicantIncome': [1400.0],
    # 'LoanAmount': [113.0],
    # 'Loan_Amount_Term': [360.0],
    # 'Credit_History': [1.0],
    # 'Property_Area': 'Urban'})

    data = pd.DataFrame.from_dict({'Gender': [i1],
    'Married': [i2],
    'Dependents': [i3],
    'Education': [i4],
    'Self_Employed': [i5],
    'ApplicantIncome': [int(i6)],
    'CoapplicantIncome': [int(i7)],
    'LoanAmount': [int(i8)],
    'Loan_Amount_Term': [int(i9)],
    'Credit_History': [int(i10)],
    'Property_Area': i11})
    
    result = loaded_model.predict(data)[0]
    if result == 'Y':
        p='Nice! Your loan would be APPROVED!!!'
    elif result == 'N':
        p = 'Sorry, your loan request might be rejected!'
    loan_detail= f'Loan amount: ${i8}K, Loan Term: {i9} months'

    return render_template("index.html",prediction_text=p,loan_detail=loan_detail)

if __name__ == "__main__":
    app.run()

