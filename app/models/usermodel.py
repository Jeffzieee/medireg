#for user and delivery user databse
from app.app import db

class User(db.Document):
	username = db.StringField(required=True)
	usermailid = db.StringField(required=True,unique=True)
	userpassword = db.StringField(required=True)
	deliveryaddress = db.ListField()
	userphoneno = db.StringField(required=True)
	cost = db.StringField()
	def is_authenticated(self):
		return True

	def get_id(self):
		return str(self.id)

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	# meta = {
	# 	'allow_inheritance': True,
	# 	'indexes': ['-date_created', 'email'],
	# 	'ordering': ['-date_created']
	# }
