#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, String, Integer, Float,
                        Table, ForeignKey)
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False))


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
    longitude = Column('longitude', Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)

    else:

        @property
        def reviews(self):
            from models import storage
            """getter function"""
            my_reviews = []
            all_reviews = list(storage.all(cls='Review').values())

            for review in all_reviews:
                if review.place_id == self.id:
                    my_reviews.append(review)
            return my_reviews

        @property
        def amenities(self):
            from models import storage
            """Returns the list of Amenity instances
            based on the attribute amenity_id that contain all
            Amenity.id linked to the place
            """
            amenities = list(storage.all(cls='Amenity').values())
            return [amnty for amnty in amenities if amnty.id in
                    self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Adds Amenity.id to the attribute amenity_ids
            It only accepts Amenity objects
            """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
