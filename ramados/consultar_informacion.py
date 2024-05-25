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

# Función para obtener el último documento insertado en una colección
def obtener_ultimo_elemento(coleccion):
    # Se asume que los documentos tienen un campo _id, que es un ObjectId y se incrementa cronológicamente
    return coleccion.find().sort([("_id", -1)]).limit(1)

# Obtener el último elemento de la colección "locales_comida"
ultimo_local_comida = obtener_ultimo_elemento(locales_comida)
for doc in ultimo_local_comida:
    print("Último local de comida:")
    print(doc)

# Obtener el último elemento de la colección "centros_deportivos"
ultimo_centro_deportivo = obtener_ultimo_elemento(centros_deportivos)
for doc in ultimo_centro_deportivo:
    print("Último centro deportivo:")
    print(doc)
