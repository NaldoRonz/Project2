from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import TextField, FileField, StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired
from werkzeug.utils import secure_filename


class RegisterForm(FlaskForm):
	Username = StringField(validators=[DataRequired])
	Password = PasswordField(validators=[DataRequired])
	Firstname = StringField(validators=[DataRequired])
	Lastname = StringField(validators=[DataRequired])
	Email = StringField(validators=[DataRequired])
	Location = StringField(validators=[DataRequired])
	Biography = TextField(validators=[DataRequired])

class LoginForm(FlaskForm):
  Username = StringField('Username', validators=[InputRequired()])
  Password = PasswordField('Password',validators=[InputRequired()])

class PostForm(FlaskForm):
  user_id = StringField("", validators=[DataRequired()])
  photo = FileField("ProfilePhoto", validators=[DataRequired()])
  caption = TextAreaField("Caption: ")

#not sure if the caption needed a validator and not too sure if DataRequired must end with the () like InputRequired(). - Kyle


#class UploadForm(FlaskForm):
#  Photo = FileField(validators=[FileRequired(), FileAllowed(["jpg","png","jpeg"])])
#  Description = TextField(validators = [DataRequired()])