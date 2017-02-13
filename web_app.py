from flask import Flask, render_template, request , redirect, url_for, session
app = Flask(__name__)
app.secret_key="this is my project"
# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base , Users , Teams , leagues , Players , games , news , gallery , leagues_teams 

from datetime import datetime

from sqlalchemy import create_engine, desc, asc

from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
dbsession = DBSession()



#YOUR WEB APP CODE GOES HERE
@app.route('/')
def main():
	return render_template('home.html')

@app.route('/sign_in', methods=['GET', 'POST'])
def signin():
	if request.method=="POST":
		name=request.form['name']
		password=request.form['password']
		user=dbsession.query(Users).filter_by(name=name,password=password).first()
		if user is None:
			return render_template('signup.html')
		return redirect(url_for('main'))
	else:
		return render_template('signIn.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	if request.method == 'POST':
		name=request.form['firstname']
		email=request.form['email']
		password=request.form['password']
		gender=request.form['gender']
		date=request.form['date']
		user=Users(name=name ,password=password, email=email,dob=date)
		dbsession.add(user)
		dbsession.commit()
		return redirect(url_for('main'))
	if request.method == 'GET':
		return render_template('signup.html')

@app.route('/leagues')
def leagues():
	return render_template('leagues.html')

@app.route('/games')
def games():
	return render_template('games.html')

@app.route('/aboutme')
def aboutme():
	return render_template('aboutme.html')


if __name__ == '__main__':
	app.run(debug=True)
