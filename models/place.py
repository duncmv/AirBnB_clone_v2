#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, String, Integer, Float, ForeignKey)
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column('city_id', String(60), ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column('user_id', String(60), ForeignKey('users.id'),
                     nullable=False)
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024))
    number_rooms = Column('number_rooms', Integer, nullable=False, default=0)
    number_bathrooms = Column('number_bathrooms', Integer, nullable=False,
                              default=0)
    max_guest = Column('max_guest', Integer, nullable=False, default=0)
    price_by_night = Column('price_by_night', Integer, nullable=False,
                            default=0)
    latitude = Column('latitude', Float)
    longitude = Column('longtitude', Float)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete_orphan')
    else:
        @property
        def reviews(self):
            """getter function"""
            from models import storage
            my_reviews = []
            all_reviews = list(storage.all(cls='Review').values())
            for review in all_reviews:
                if review.place_id == self.id:
                    my_reviews.append(review)
            return my_reviews

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
