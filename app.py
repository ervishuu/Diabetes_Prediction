from flask import Flask,render_template,request,jsonify
import pickle

import joblib
model = joblib.load("Diabetes_Pred.pkl")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict',methods=['POST'])
def predict():
  if request.method == "POST" :

     Glucose = float(request.form["Glucose"])
     BloodPressure = float(request.form["BloodPressure"])
     SkinThickness = float(request.form["SkinThickness"])
     Insulin = float(request.form["Insulin"])
     BMI = float(request.form["BMI"])
     DiabetesPedigreeFunction = float(request.form["DiabetesPedigreeFunction"])
     Age = float(request.form["Age"])

     data =[[Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
     print(data)

     result  = model.predict(data)
     print(result)


     if result[0] == 0:
         return render_template('index.html',data=["Negative!! You do not have diabetes","green"])


     elif result[0] == 1:
         return render_template('index.html', data=["Positive!! You have diabetes", "red"])


if __name__ == "__main__":
    app.run(debug=True)