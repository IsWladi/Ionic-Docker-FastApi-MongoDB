# This api will be requested by the ionic app
from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
import json

app = FastAPI()

# Configurar las credenciales de autenticación
username = "admin"
password = "myPass123"

# Crear una instancia del cliente de MongoDB
mongo_client = MongoClient("mongodb://mongo_db_dev:27017/",
                           username=username,
                           password=password)

# Obtener una referencia a la base de datos
mongo_db = mongo_client["test_ionic"]
usuarios_collection = mongo_db["usuarios"]

@app.get("/")
def root():
    documentos = usuarios_collection.find()
    usuarios = [dumps(doc) for doc in documentos]
    usuarios = [json.loads(usuario) for usuario in usuarios]
    for usuario in usuarios:
        usuario["_id"] = str(usuario["_id"])  # Convertir ObjectId a cadena
    return usuarios
