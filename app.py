import datetime

from flask import request
import pandas as pd

from ms import app #Lógica del microservicio
from ms.functions import get_model_response 

model_name = "Breast Cancer Wisconsin (Diagnostic)"
model_file = 'model_binary.dat.gz' #Modelo creado en train
version = "v1.0.0"

#Ruta para dar información del modelo (nombre y versión)
@app.route('/info' , methods = ['GET'])
def info():

    result = {}

    result["name"] = model_name
    result["version"] = version 

    return result 

#Para monitorear que el modelo está activo
@app.route('/health' , methods = ['GET'])
def health():

    return 'ok'

#Toma las variables, las pasa por el modelo y regresa la predicción
@app.route('/predict', methods = ['POST'])
def predict():

    feature_dict = request.get_json()

    if not feature_dict:

        return {
            'error' : 'Body is empty'
        } , 500

    try:

        response = get_model_response(feature_dict) #Se pasa el json del request al modelo

    except ValueError as e:

        return {'error' : str(e).split('\n')[-1].strip()} , 500

    return response , 200

if __name__ == '__main__':

    app.run(host = '0.0.0.0')