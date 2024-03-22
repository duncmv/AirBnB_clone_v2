#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the DBStorage class"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.reflect(bind=self.__engine)
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query the session and return a dictionary of all objs"""
        classes = {'User': User, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review}
        objs = {}
        if cls is None:
            for key in classes:
                query = self.__session.query(classes[key]).all()
                for obj in query:
                    objs[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            if f"{cls}" in classes.keys():
                query = self.__session.query(classes[f"{cls}"])
                for obj in query:
                    objs[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return objs

    def new(self, obj):
        """adds new object to database"""
        self.__session.add(obj)

    def save(self):
        """commits all changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from database"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """creates all tables and session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """closes the session"""
        self.__session.close()
