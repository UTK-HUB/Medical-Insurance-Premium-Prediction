from flask import Flask, request, jsonify, render_template
from utils import Medical_Insurance
import numpy as np
import config

app = Flask(__name__)

@app.route('/insurance_html')
def index():
    return render_template('index.html')

@app.route('/predict_premium', methods=['POST', 'GET'])
def get_insurance():
    if request.method == 'POST':
        data = request.form
        print("User input data:", data)
        age = eval(data['age'])
        gender = data['gender']
        bmi = eval(data['bmi'])
        children = int(data['children'])
        smoker = data['smoker']
        region = data['region']
        
        obj = Medical_Insurance(age, gender, bmi, children, smoker, region)
        premium = obj.get_predict_premium()
        return jsonify({'Result': f'Predicted medical insurance premium is {premium[0]}'})
    else:
        return 'Invalid request method'

if __name__ == '__main__':
    app.run(host="localhost", port=config.port_number, debug=False)
