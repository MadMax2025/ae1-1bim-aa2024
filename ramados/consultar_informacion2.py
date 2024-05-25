"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# Conexión a la base de datos
db = client.propiedad_venta

# Colección "locales_comida"
locales_comida = db["locales_comida"]

# Colección "centros_deportivos"
centros_deportivos = db["centros_deportivos"]

# Función para obtener el documento con la mayor capacidad de una colección
def obtener_mayor_capacidad(coleccion):
    # Se asume que los documentos tienen un campo "capacidad_personas" que es un número
    return coleccion.find().sort([("capacidad_personas", -1)]).limit(1)

# Obtener el documento con la mayor capacidad de la colección "locales_comida"
local_comida_mayor_capacidad = obtener_mayor_capacidad(locales_comida)
for doc in local_comida_mayor_capacidad:
    print("Local de comida con mayor capacidad:")
    print(doc)

# Obtener el documento con la mayor capacidad de la colección "centros_deportivos"
centro_deportivo_mayor_capacidad = obtener_mayor_capacidad(centros_deportivos)
for doc in centro_deportivo_mayor_capacidad:
    print("Centro deportivo con mayor capacidad:")
    print(doc)
