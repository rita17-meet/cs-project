from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import 
from datetime import datetime

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#You can add some starter data for your database here.

