from flask import Flask,request,jsonify
import config
from LP_Medical_insurance.utils import Medical_Insurance
import numpy as np

app = Flask(__name__)
@app.route('/')
def get_home():
    return "Hello!, Welcome to Medical Insurance"

@app.route('/predict_premium',methods=['POST','GET'])
def get_insurance():
    if request.method == 'POST':
        data = request.form
        print("User input data :",data)
        age = eval(data['age'])
        gender = data['gender']
        bmi = eval(data['bmi'])
        children = int(data['children'])
        smoker = data['smoker']
        region = data['region']
        obj = Medical_Insurance(age,gender,bmi,children,smoker,region)
        premium = obj.get_predict_premium()
        return jsonify({'Result':f'Predicted medical insurance premium is {premium[0]}'} )
        

if __name__=='__main__':
    app.run()