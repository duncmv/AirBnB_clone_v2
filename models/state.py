#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)
