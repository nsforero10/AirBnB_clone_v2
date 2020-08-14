#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBTN_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', cascade='all, delete-orphan', backref='state')

    else:
        @property
        def cities(self):
            '''Returns list of citiy where dstate_id is equal to State.id'''
            instance_list = []
            for _, val in models.storage.all().items():
                if val.__class__.__name__ == 'City'\
                        and val.state._id == self.id:
                    instance_list.append(val)
            return instance_list
