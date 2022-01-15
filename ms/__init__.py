from flask import Flask
import joblib

#Se declara la aplicación
app = Flask(__name__)

#Se carga el modelo
model = joblib.load('model/model_binary.dat.gz')