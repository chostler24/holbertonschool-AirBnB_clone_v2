#!/usr/bin/python3
""" Place Module for HBNB project """
from ast import In, Str
from re import I
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(0), nullable=False)
    number_bathrooms = Column(Integer(0), nullable=False)
    max_guest = Column(Integer(0), nullable=False)
    price_by_night = Column(Integer(0), nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    __tablename__ = "places"

