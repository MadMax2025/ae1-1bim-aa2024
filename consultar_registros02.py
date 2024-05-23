from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import centrosDeportivos
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# Obtener todos los registros de la entidad Autor con una(s) condición.
# Se hace uso del método query.
# filter, permite agregrar condiciones a la búsqueda, con base
# a las propiedades de la entidad
lista_centros = session.query(centrosDeportivos).filter(centrosDeportivos.capacidad>300)
# La variable lista_autores, tendrá un listado de objetos de tipo Autor que
# tengan en la propiedad de nacionalidad el valor: ecuatoriana


# se realiza un proceso iterativo para presentar la información
# de cada objeto.
for l in lista_centros:
    print(l)
