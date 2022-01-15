# Este es un ejercicio realizado en el data live "De la Ciencia de Datos al MLOps".


## Para probar antes de obtener el Dockerfile: 


flask run -p 5000


## Se probó en Postman utilizando el documento "example.json" dentro de la carpeta test.


## Para obtener la imagen (el Dockerfile):


docker build . -t mlops_datalive


## Para probar:


docker run -p 5000:5000 mlops_datalive