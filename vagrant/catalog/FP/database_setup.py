import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# this is a good sql alchemy reference
# http://bytefish.de/blog/first_steps_with_sqlalchemy/
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'email': self.email,
            'picture': self.picture
        }
print "created user"


class Vitamin(Base):
    __tablename__ = 'vitamin'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    MinimumIntake = Column(String(250))
    description = Column(String(250))
    longDescription = Column(String(250))
    foodImageName = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'MinimumIntake': self.MinimumIntake,
            'foodImageName': self.foodImageName
        }

print "created vitamin"


class FoodSource(Base):
    __tablename__ = 'foodSource'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    serving = Column(String(8))
    amount = Column(String(250))
    vitamin_id = Column(Integer, ForeignKey('vitamin.id'))
    vitamin = relationship(Vitamin)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'serving': self.serving,
            'amount': self.amount,
        }


engine = create_engine('sqlite:///vitaminCatalog.db', echo=True)


Base.metadata.create_all(engine)
