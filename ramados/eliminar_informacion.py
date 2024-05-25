"""
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# Conexión a la base de datos
db = client.propiedad_venta

# Colección "locales_comida"
locales_comida = db["locales_comida"]

# Función para encontrar y eliminar el documento con la menor capacidad de una colección
def eliminar_menor_capacidad(coleccion):
    # Encontrar el documento con la menor capacidad de personas
    menor_capacidad_doc = coleccion.find().sort([("capacidad_personas", 1)]).limit(1)
    for doc in menor_capacidad_doc:
        print("Eliminando el siguiente documento con menor capacidad:")
        print(doc)
        # Eliminar el documento encontrado
        coleccion.delete_one({"_id": doc["_id"]})
