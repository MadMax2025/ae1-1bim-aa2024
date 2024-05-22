from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import Autor
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

# se crea un objetos de tipo Autor
autor1 = Autor(nombre="José", apellido="Armijos", nacionalidad="ecuatoriana",
        edad=40)
autor2 = Autor(nombre="Sara", apellido="Benitez", nacionalidad="colombiana",
        edad=20)
autor3 = Autor(nombre="Pedro", apellido="Díaz", nacionalidad="peruana",
        edad=35)
autor4 = Autor(nombre="Mónica", apellido="Carrión", nacionalidad="ecuatoriana",
        edad=25)
# se agrega los objetos de tipo Autor a la sesión
# a la espera de un commit
session.add(autor1)
session.add(autor2)
session.add(autor3)
session.add(autor4)

# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()
