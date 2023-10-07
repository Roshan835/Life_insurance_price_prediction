from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict_placement():
    age = int(request.form.get('age'))
    bmi = float(request.form.get('bmi'))
    children = int(request.form.get('children'))
    gender = int(request.form.get('gender'))
    smoker = int(request.form.get('smoker'))
    region = int(request.form.get('region'))

    result = model.predict(np.array([age,gender,bmi,children,smoker,region]).reshape(1,6))
    return render_template('index.html',result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
