from flask import Flask, request, jsonify

# import joblib
import numpy as np
import pickle

with open('SF_DataScience/Блок 7. ML в бизнесе/5. DS_PROD-1. Подготовка модели к продакшену и деплой/data/model.pkl', 'rb') as pkl_file: 
    model = pickle.load(pkl_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def get_pred():
    features = np.array(request.json)
    features = features.reshape(1, 4)
    pred = model.predict(features)
    return {"prediction": pred[0]}

    
if __name__ == '__main__':

    app.run('localhost', 5000)