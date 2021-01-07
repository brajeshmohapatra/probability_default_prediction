from flask import Flask, render_template, request
import requests
import jsonify
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__, template_folder='templates')
model = pickle.load(open(r'C:\\Users\\Brajesh Mohapatra\\Python\\Probability of Default Prediction\\probability_default_prediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['aa'])
        income = float(request.form['ab'])
        home_ownership = request.form['ac']
        if home_ownership == 'Own':
            home_ownership_own = 1
            home_ownership_rent = 0
            home_ownership_mortgage = 0
            home_ownership_other = 0
        elif home_ownership == 'Rent':
            home_ownership_own = 0
            home_ownership_rent = 1
            home_ownership_mortgage = 0
            home_ownership_other = 0
        elif home_ownership == 'Mortgage':
            home_ownership_own = 0
            home_ownership_rent = 0
            home_ownership_mortgage = 1
            home_ownership_other = 0
        else:
            home_ownership_own = 0
            home_ownership_rent = 0
            home_ownership_mortgage = 0
            home_ownership_other = 1
        y_o_e = float(request.form['ad'])
        loan_purpose = request.form['ae']
        if loan_purpose == 'Debt Consolidation':
            loan_pupose_dc = 1
            loan_purpose_e = 0
            loan_purpose_hi = 0
            loan_purpose_m = 0
            loan_purpose_p = 0
            loan_purpose_v = 0
        elif loan_purpose == 'Education':
            loan_pupose_dc = 0
            loan_purpose_e = 1
            loan_purpose_hi = 0
            loan_purpose_m = 0
            loan_purpose_p = 0
            loan_purpose_v = 0
        elif loan_purpose == 'Home Improvement':
            loan_pupose_dc = 0
            loan_purpose_e = 0
            loan_purpose_hi = 1
            loan_purpose_m = 0
            loan_purpose_p = 0
            loan_purpose_v = 0
        elif loan_purpose == 'Medical':
            loan_pupose_dc = 0
            loan_purpose_e = 0
            loan_purpose_hi = 0
            loan_purpose_m = 1
            loan_purpose_p = 0
            loan_purpose_v = 0
        elif loan_purpose == 'Personal':
            loan_pupose_dc = 0
            loan_purpose_e = 0
            loan_purpose_hi = 0
            loan_purpose_m = 0
            loan_purpose_p = 1
            loan_purpose_v = 0
        else:
            loan_pupose_dc = 0
            loan_purpose_e = 0
            loan_purpose_hi = 0
            loan_purpose_m = 0
            loan_purpose_p = 0
            loan_purpose_v = 1
        loan_grade = request.form['af']
        if loan_grade == 'A':
            loan_grade_a = 1
            loan_grade_b = 0
            loan_grade_c = 0
            loan_grade_d = 0
            loan_grade_e = 0
            loan_grade_f = 0
            loan_grade_g = 0
        elif loan_grade == 'B':
            loan_grade_a = 0
            loan_grade_b = 1
            loan_grade_c = 0
            loan_grade_d = 0
            loan_grade_e = 0
            loan_grade_f = 0
            loan_grade_g = 0
        elif loan_grade == 'C':
            loan_grade_a = 0
            loan_grade_b = 0
            loan_grade_c = 1
            loan_grade_d = 0
            loan_grade_e = 0
            loan_grade_f = 0
            loan_grade_g = 0
        elif loan_grade == 'D':
            loan_grade_a = 0
            loan_grade_b = 0
            loan_grade_c = 0
            loan_grade_d = 1
            loan_grade_e = 0
            loan_grade_f = 0
            loan_grade_g = 0
        elif loan_grade == 'E':
            loan_grade_a = 0
            loan_grade_b = 0
            loan_grade_c = 0
            loan_grade_d = 0
            loan_grade_e = 1
            loan_grade_f = 0
            loan_grade_g = 0
        elif loan_grade == 'F':
            loan_grade_a = 0
            loan_grade_b = 0
            loan_grade_c = 0
            loan_grade_d = 0
            loan_grade_e = 0
            loan_grade_f = 1
            loan_grade_g = 0
        else:
            loan_grade_a = 0
            loan_grade_b = 0
            loan_grade_c = 0
            loan_grade_d = 0
            loan_grade_e = 0
            loan_grade_f = 0
            loan_grade_g = 1
        loan_amount = float(request.form['ag'])
        roi = float(request.form['ah'])
        loan_percentage_income = round((loan_amount * 100) / income, 2)
        default_history = request.form['ai']
        if default_history == 'Yes':
            default_history = 1
        else:
            default_history = 0
        y_o_credit_history = float(request.form['aj'])
        entries = np.array([loan_percentage_income, income, roi, loan_amount, loan_grade_d, home_ownership_rent, y_o_e, age, y_o_credit_history, loan_grade_e])
        entries = entries.reshape(1, -1)
        prediction = model.predict_proba(entries)
        output = prediction[0][1] * 100
        output = output.round(decimals = 0)
        return render_template('index.html', prediction_text = "The risk of credit default is {}%".format(output))
    else:
        return render_template('index.html')
if __name__=="__main__":
    #app.run(host = '0.0.0.0', port = 8080)
    app.run(debug = True)