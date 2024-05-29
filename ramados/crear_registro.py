import pymongo
from enlace_base import client
# Conexión a la base de datos

db = client.propiedad_venta

# Colección "locales_comida"
locales_comida = db["locales_comida"]

# Nuevo registro a subir
nuevo_local_comida = {
    "nombre": "Restaurante La Parrilla",
    "localidad": "Quito",
    "direccion": "Av. 10 de Agosto y Amazonas",
    "capacidad_personas": 80
}

# Insertar el nuevo registro
locales_comida.insert_one(nuevo_local_comida)

print("Nuevo registro subido exitosamente!")
