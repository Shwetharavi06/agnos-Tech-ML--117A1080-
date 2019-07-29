from flask import Blueprint,request,jsonify
import pickle

model=pickle.load(open(ml.py,'rb'))


model_predict = Blueprint('model_predictor')

@model_predict.route('/predict',methods=['POST'])
def predict_value():
    sepal_length = request.get_json['sepal_length']
    sepal_width = request.get_json['sepal_width']
    petal_length = request.get_json['petal_length']
    petal_width = request.get_json['petal_width']
model.predict([sepal_length,sepal_width,petal_length,petal_width])
print(prediction)
    