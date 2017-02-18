from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()



class Users(Base):
	__tablename__="users"
	id=Column(Integer, primary_key=True)
	name=Column(String)
	email=Column(String)
	password=Column(String)
	dob=Column(String(255))
	gender=Column(String)

class Teams(Base):
	__tablename__="teams"
	id=Column(Integer,primary_key=True)
	name=Column(String)
	picture=Column(String)

class leagues(Base):
	__tablename__="leagues"
	id=Column(Integer,primary_key=True)
	name=Column(String)
	location=Column(String)

class Players(Base):
	__tablename__="players"
	id=Column(Integer,primary_key=True)
	name=Column(String)
	gender=Column(String)
	city=Column(String)
	DOB=Column(String)
	team_id=Column(Integer,ForeignKey('teams.id'))

class Games(Base):
	__tablename__="games"
	id=Column(Integer,primary_key=True)
	league_id=Column(Integer, ForeignKey('leagues.id'))
	team1=Column(Integer, ForeignKey('teams.id'))
	team2=Column(Integer, ForeignKey('teams.id'))
	location=Column(String)
	date=Column(String)

class news(Base):
	__tablename__="news"
	id=Column(Integer,primary_key=True)
	subject=Column(String)
	Date=Column(String)
	content=Column(String)

class gallery(Base):
	__tablename__="gallery"
	id=Column(Integer,primary_key=True)
	type1=Column(String)
	name=Column(String)
	news_id=Column(Integer,ForeignKey('news.id'))

class leagues_teams(Base):
	__tablename__="leagues_teams"
	id=Column(Integer,primary_key=True)
	league_id=Column(Integer,ForeignKey('leagues.id'))	
	team_id=Column(Integer,ForeignKey('teams.id'))
	rank=Column(Integer)

engine = create_engine('sqlite:///Project.db')


Base.metadata.create_all(engine)


