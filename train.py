from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC 
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import ConfusionMatrixDisplay

import matplotlib.pyplot as plt
import pandas as pd
import joblib
import gzip
import pdb

#pdb.set_trace() #Pone un break point

data = pd.read_csv('data/breast_cancer.csv')


data = data.set_index('id')

del data['Unnamed: 32']

data['diagnosis'] = data['diagnosis'].replace(['B' , 'M'] , [0 , 1]) #Encode benigno -> 0, maligno -> 1

#Se hace split de los datos
y = data.pop('diagnosis')

X = data

X_train , X_test , y_train , y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

pdb.set_trace()
#Se hace un Voting Classifier, se toman 3 modelos y se combinará la decisión de los 3
estimators = []
estimators.append(('logistic' , LogisticRegression()))
estimators.append(('cart' , DecisionTreeClassifier()))
estimators.append(('svm' , SVC()))

#Se crea ensamble del modelo
ensemble  = VotingClassifier(estimators)

#Se crea el Pipeline de preproceso, procesos o alteraciones que seguirán los datos previo a generar
#una predicción
pipe = Pipeline([
    ('imputer' , SimpleImputer()), #Para rellenar datos faltantes 
    ('scaler' , MinMaxScaler(feature_range = (0 , 1))), #Para escalar variables numéricas
    ('model' , ensemble)
])

pipe.fit(X_train , y_train)

#Test Accuracy
print("Accuracy: %s" % str(pipe.score(X_test , y_test)))

#Confusion Matrix
print(ConfusionMatrixDisplay.from_estimator(pipe, X_test, y_test))
plt.show()

pdb.set_trace()

#Se exporta el modelo como artefacto. Cuando se cargue la aplicación tomará este modelo
joblib.dump(pipe, gzip.open('model/model_binary.dat.gz', "wb"))