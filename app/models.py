from app import *
from app.settings import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from sqlalchemy import ForeignKey
from datetime import datetime

class User(db.Model):
        # name of table
	__tablename__ = 'user_details'
	
	id = db.Column(db.BigInteger, primary_key=True)
	username = db.Column(db.String(60), unique=True)
	password = db.Column(db.String(500))
	email = db.Column(db.String(60), unique=True)
	create_at = db.Column(
		db.TIMESTAMP,
		default=datetime.utcnow,
		nullable=False
	)

	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email


	# Flask-Login integration
	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

class details(db.Model):
        # name of table  
	__tablename__ = 'users_insights'

	id = db.Column(
        db.BigInteger,
        primary_key=True)
        
	# foreign key is used to set the relationship. Primary key of one table is 
	# used as the foreign key of another table.
	user_id = db.Column(
		db.BigInteger,
		ForeignKey('user_details.id')
	)
        # since we can have large output returned, hence datatype is Text.
	frequency_count = db.Column(db.Text,unique=True)
    
	def __init__(self, user_id, frequency_count):
		self.user_id = user_id
		self.frequency_count = frequency_count
		
     
     
