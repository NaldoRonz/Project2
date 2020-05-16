from . import db
from werkzeug.security import generate_password_hash

class Likes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)

    def __init__(self,post_id,user_id):
        self.user_id = user_id
        self.post_id = post_id

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    photo = db.Column(db.String(255))
    caption = db.Column(db.String(255))
    created_on = db.Column(db.String(50))

class Follows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    follower_id = db.Column(db.Integer)

    def __init__(self,user_id,follower_id):
        self.user_id = user_id
        self.follower_id = follower_id

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
      profile_photo = db.Column(db.String(30), nullable=False)
      joined_on = db.Column(db.String(20), nullable=False)

      def __init__(self,username,password,firstname,lastname,email,location,biography,profile_photo,joined_on):
      	self.username = username
      	self.password = password
      	self.firstname = firstname
      	self.lastname = lastname
      	self.email = email
      	self.location = location
      	self.biography = biography
      	self.joined_on = joined_on
      	self.profile_photo = profile_photo

def __repr__(self):
	return f"my_users('{self.username}','{self.password}','{self.firstname}','{self.lastname}','{self.email}','{self.location}','{self.biography}','{self.profile_photo}','{self.joined_on}')"


#class my_posts(db.Model):
#	_tablename_ = "user_posts"

class Likes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)

    def __init__(self,post_id,user_id):
        self.user_id = user_id
        self.post_id = post_id

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    photo = db.Column(db.String(255))
    caption = db.Column(db.String(255))
    created_on = db.Column(db.String(50))

class Follows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    follower_id = db.Column(db.Integer)

    def __init__(self,user_id,follower_id):
        self.user_id = user_id
        self.follower_id = follower_id


db.create_all() 