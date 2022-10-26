#!/usr/bin/python3
""" Place Module for HBNB project """
from ast import In, Str
from re import I
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, backref

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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

    reviews = relationship(
        'Review',
        backref='state',
        cascade='all, delete-orphan')

    @property
    def reviews(self):
        """ getter that returns list of Reviews instances """
        instances = models.storage.all(Review)
        new = []
        for reviews in instances.values():
            if reviews.place_id == (self.id):
                new.append(review)
        return new