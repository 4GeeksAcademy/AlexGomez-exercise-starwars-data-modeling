import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    fecha_subscripcion = Column(DateTime, nullable=False)
    

class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    clima = Column(String, nullable=True)
    terreno = Column(String, nullable=True)
    poblacion = Column(Integer, nullable=True)
   

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    genero = Column(String, nullable=True)
    altura = Column(Integer, nullable=True)
    peso = Column(Integer, nullable=True)
    especie = Column(String, nullable=True)
class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    modelo = Column(String, nullable=True)
    costo = Column(Integer, nullable=True)
    combustible = Column(Integer, nullable=True)
    asientos = Column(Integer, nullable=True)

class Favorito(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planetas.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personajes.id'), nullable=False)
    vehiculo_id = Column(Integer, ForeignKey('vehiculos.id'), nullable=False)


    usuario = relationship('usuario')
    planeta = relationship('planeta')
    personaje = relationship('personaje')
    vehiculo = relationship('vehiculo')

render_er(Base, 'diagram.png')
