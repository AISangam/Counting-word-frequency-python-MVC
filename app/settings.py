import os
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, \
	logout_user, current_user

template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(
	__name__,
	template_folder = template_dir,
	static_folder = static_dir)

app.config["SECRET_KEY"] = "this_is_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@db:3306/frequency_occurence'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)	
