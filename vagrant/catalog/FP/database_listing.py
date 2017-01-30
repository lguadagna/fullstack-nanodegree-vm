import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import inspect
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from database_setup import Vitamin, Base, FoodSource, User

Base = declarative_base()

engine = create_engine('sqlite:///vitaminCatalog.db', echo=True)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# a collection of meta data entities is stored in an object called metaData
metadata = MetaData()

u = session.query(User).all()
print u

v = session.query(Vitamin).all()

print v



for t in metadata.sorted_tables:
    print t
    
for c in Vitamin.c:
    print(c)
    
    



