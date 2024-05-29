"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# Importación individual de colecciones
db = client.propiedad_venta
# Colección "locales_comida"
locales_comida = db["locales_comida"]

# Elemento 1
local_comida1 = {
    "nombre": "Restaurante La Fogata",
    "localidad": "Quito",
    "direccion": "Av. 12 de Octubre y Shyris",
    "capacidad_personas": 50
}

# Elemento 2
local_comida2 = {
    "nombre": "Pizzería Italia",
    "localidad": "Guayaquil",
    "direccion": "Calle Rocafuerte y 9 de Octubre",
    "capacidad_personas": 30
}

locales_comida.insert_many([local_comida1, local_comida2])

# Colección "centros_deportivos"
centros_deportivos = db["centros_deportivos"]
# Elemento 1
centro_deportivo1 = {
    "nombre": "Gimnasio Los Titanes",
    "localidad": "Cuenca",
    "direccion": "Calle Bolívar y Juan Montalvo",
    "capacidad_personas": 100
}

# Elemento 2
centro_deportivo2 = {
    "nombre": "Piscina Olímpica",
    "localidad": "Ambato",
    "direccion": "Av. Cevallos y Av. Manta",
    "capacidad_personas": 200
}

centros_deportivos.insert_many([centro_deportivo1, centro_deportivo2])

