import pandas as pd
from ms import model

def predict(X, model):

    prediction = model.predict(X)[0]

    return prediction

def get_model_response(json_data): #Recibe el json

    X = pd.DataFrame.from_dict(json_data)
    prediction = predict(X , model) #Le pasa el vector de variables y el modelo y regresa una predicción

    if prediction == 1:

        label = "M"

    else:

        label = "B"

    return {
        'status' : 200 ,
        'label' : label , 
        'prediction' : int(prediction)
    }