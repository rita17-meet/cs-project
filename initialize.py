from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import 
from datetime import datetime

from database_setup import Base , Users , Teams , leagues , Players , Games , news , gallery , leagues_teams 

engine = create_engine('sqlite:///Project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#You can add some starter data for your database here.

