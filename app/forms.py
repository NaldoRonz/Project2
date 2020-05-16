from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import TextField, FileField, StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired
from werkzeug.utils import secure_filename


class RegisterForm(FlaskForm):
	Username = StringField('Username',validators=[DataRequired])
	Password = PasswordField('Password',validators=[DataRequired])
	Firstname = StringField('Firstname',validators=[DataRequired])
	Lastname = StringField('Lastname',validators=[DataRequired])
	Email = StringField('email',validators=[DataRequired])
	Location = StringField('location',validators=[DataRequired])
	Biography = TextAreaField('Biography',validators=[DataRequired])
  photo = FileField('ProfilePhoto', validators=[FileRequired(), FileAllowed('jpg','png','jpeg')])

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