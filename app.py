# IMPORTS
import os
import joblib
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


# Flask Setup
app = Flask(__name__)
# loaded_model = joblib.load(filename)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

    
# route for PREDICTIONS
@app.route("/predict", methods=['POST'])
def predict():
    return '<h1> ****** LOAN APPROVAL PENDING ****** </h1>' 


if __name__ == "__main__":
    app.run()

