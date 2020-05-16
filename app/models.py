from . import db

class my_users(db.Model):
      _tablename_ = "user_profiles"

      user_id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(50), nullable=False, unique=True)
      password = db.Column(db.String(30), nullable=False)
      firstname = db.Column(db.String(30), nullable=False)
      lastname = db.Column(db.String(30), nullable=False)
      email = db.Column(db.String(30), nullable=False, unique=True)
      location = db.Column(db.String(30), nullable=False)
      biography = db.Column(db.String(300), nullable=False)
      joined_on = db.Column(db.String(20), nullable=False)

      def __init__(self,username,password,firstname,lastname,email,location,biography,joined_on):
      	self.username = username
      	self.password = password
      	self.firstname = firstname
      	self.lastname = lastname
      	self.email = email
      	self.location = location
      	self.biography = biography
      	self.joined_on = joined_on

    def __repr__(self):
        return f"my_users('{self.username}','{self.password}','{self.firstname}','{self.lastname}','{self.email}','{self.location}','{self.biography}','{self.joined_on}')"


class my_posts(db,Model):
	_tablename_ = "user_posts"

	

    db.create_all() 