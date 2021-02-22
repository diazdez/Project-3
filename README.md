# Project-3

### **Team:** Desiree Diaz, Medina Izgutdina, Irene Okada, Wei Zhu 

The goal of our project was to develop a classification machine learning model predicting a house loan approval. 

In order to train our model, we obtained the data from [kaggle](https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset). The dataset of approved and rejected loans included demographic information of applicants (gender, marital status, number of dependents, education) as well as some financial data (whether or not the applicant is self-employed, applicant and co-applicant income (monthly), loan amount (thousands), loan term (months), and presence of credit history).

Using **Tableau**, we analyzed trends and patterns in our data. The analysis provided us with important insights that we were mindful of while creating and training the model. Thus, from the training dataset analysis we learned that 
* There were more approved loans in suburban, followed by urban and rural areas 
* There were more approved loans for males than females 
* More married applicants were approved for loans 
* Average approved loan amounts were higher for graduates and those with a larger number of dependents. 

While developing a predictive classification model, we utilized **pipeline** method to optimize the coding process and standardize the workflow. This approach helped us streamline data pre-processing and transformation of categorical values. The machine learning model we used is **Gradient Boosting Classifier**. The model accuracy was found to be **85%**.    

Finally, we developed a website where a user can input their demographic information and test whether or not the requested loan will be approved. We utilized **Flask** to deploy our model and **Heroku** to host the website.

Check it out: [Website](https://loan-predictions.herokuapp.com/)

#### **Dependencies**
* Flask
* HTML/CSS/Bootstrap
* Python Pandas
* Scikit-Learn
* Tableau
