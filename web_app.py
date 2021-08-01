from flask import Flask,render_template
from flask import request

from keras.models import load_model


m=load_model("diabetes_model.h5")

app=Flask("predict")
 
@app.route("/home")

def home():
    return render_template("diabetes.html")


@app.route("/output",methods=["GET"])
def predict():
    m=load_model("diabetes_model.h5")
    a1=(float)(request.values.get("x1"))
    a2=float(request.values.get("x2"))
    a3=float(request.values.get("x3"))
    a4=float(request.values.get("x4"))
    a5=float(request.values.get("x5"))
    a6=float(request.values.get("x6"))
    a7=float(request.values.get("x7"))

    a8=float(request.values.get("x8"))
    output=m.predict([[a1,a2,a3,a4,a5,a6,a7,a8]])
    if output < 0.5:
        return("Diabetes is not predicted for you")
    else:
        return("Diabetes is predicted for you")   

app.run(host="172.17.0.2",debug=True,port=5000)
