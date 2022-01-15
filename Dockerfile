#Para contenerizar 

#Para que se utilice la misma versión
FROM python:3.8

#Se genera archivo de trabajo
WORKDIR /app

#Se copian los archivos necesarios para correr la aplicación
COPY app.py /app
COPY requirements.txt /app
COPY model /app/model
COPY ms /app/ms

RUN pip install -r requirements.txt

#Expose del puerto por el que se va a consumir 
EXPOSE 5000
#Comando para levantar el servicio, guinicorn va a estar escuchando por el puerto 5,000
ENTRYPOINT ["gunicorn" , "-b" , "0.0.0.0:5000" , "--access-logfile" , "-" , "--error-logfile" , "-" , "--timeout" , "120"]
CMD ["app:app"]