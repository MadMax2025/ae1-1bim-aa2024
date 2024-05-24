from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import localesComida, centrosDeportivos
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

# se crea un objetos de tipo locales_comida
comercial1 = localesComida(nombreLocal="Conchitas Asadas", localidad="Quito",    direccion="Av. Pichincha", capacidad=80)
comercial2 = localesComida(nombreLocal="Rincon del Sabor", localidad="Calderon", direccion="Av. Guayaquil", capacidad=100)
comercial3 = localesComida(nombreLocal="La Foch",          localidad="Centro",   direccion="Av. Amazonas",  capacidad=120)
        

# a la espera de un commit
session.add( comercial1 )     
session.add( comercial2 )
session.add( comercial3 )

# se crea un objetos de tipo centros_deportivos
centro1 = centrosDeportivos(nombreCentro="Concentracion de futbol", localidad="Quito", tamano="Coliseo", capacidad=300)
centro2 = centrosDeportivos(nombreCentro="Polideportivo del Sur",   localidad="Quito", tamano="Estadio", capacidad=500) 

        
# a la espera de un commit
session.add( centro1)
session.add( centro2)
# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()
