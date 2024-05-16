import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Enum

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    
class Country(Base):
    __tablename__='country'
    id=Column(Integer,primary_key=True)
    name = Column(String(250))

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    Name=Column(String(50))
    email=Column(String(50),unique=True)
    password=Column(String(32))
    id_country=Column(Integer,ForeignKey('country.id'))
    country=relationship(Country)

class Planets(Base):
    __tablename__='planets'
    id=Column(Integer,primary_key=True)
    name=Column(String(50))
    population=Column(Integer)

class FavoritePlanet(Base):
    __tablename__='favorite_planet'
    id=Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user=relationship(User)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet=relationship(Planets)





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
