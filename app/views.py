from app import *
from app.settings import *
from flask import Flask, render_template, url_for, request, flash, redirect
from app.models import User
from app.code_functions import frequency_occurence
import traceback
import json

@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
	return redirect('/login')

@login_manager.user_loader
def load_user(id):
	print('[%s]' % db.session.query(User).get(id))
	return db.session.query(User).get(id)


def home_page():
	return render_template('aisangam.html')


def register_view():
	
	if request.method == 'POST':
		Username = request.form.get('uname')
		Password = request.form.get('psw')
		Email = request.form.get('email')

		user = User(
			username=Username,
			password=Password,
			email=Email
		)

		db.session.add(user)
		db.session.commit()
		return render_template('register.html')

	return render_template('register.html')  


def login_view():

	if request.method == "POST":
		try:
			Username = request.form.get('uname')
			Password = request.form.get('psw')
			user = User.query.filter_by(username=Username).first()
			if user:
				if user.password == Password:
					login_user(user)
					return redirect('/')
				else:
					raise Exception
					
		except Exception: 
			msg= "Username and password does not match"
			return ("Please enter the correct credentials")
	return render_template('login.html')


# @login_required
def nlp_freq_occurence():
	
    if request.method == "POST":
    	TEXT = request.form.get('Text1')
    	output = frequency_occurence(TEXT)  
    	# print("++++++", output)
    	return json.dumps(output)

    return render_template ('text.html')	



def logout_view():
	logout_user()
	return redirect('/	')	
	

                    





