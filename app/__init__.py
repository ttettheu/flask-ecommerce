from flask import Flask  #Importa a biblioteca



app = Flask(__name__) #Inicializa a aplicação

from app.controllers import default

