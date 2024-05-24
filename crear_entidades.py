from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
Base = declarative_base()

# Se crea la una entidad llamada Autor, que hereda
# de Base
class localesComida(Base):
    __tablename__ = 'locales comida' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreLocal = Column(String) # atributo de tipo String
    localidad = Column(String)
    direccion = Column(String)
    capacidad = Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.nombreLocal, self.localidad, self.direccion,
        self.capacidad)

class centrosDeportivos(Base):
     __tablename__ = 'centros deportivos' # El nombre de la entidad en sqlite
     
     id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
     nombreCentro = Column(String) # atributo de tipo String
     localidad = Column(String)
     tamano = Column(String)
     capacidad = Column(Integer)

     def __str__(self):
        return "%s %s %s %s" % (self.nombreCentro, self.localidad, self.tamano,
        self.capacidad)
    
# El nombre de la entidad en sqlite    
# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)
