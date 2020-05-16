from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import TextField, FileField, StringField, PasswordField
from wtforms.validators import Required
from werkzeug.utils import secure_filename


class RegisterForm(FlaskForm):
	Username = StringField(validators=[Required()])
	Password = PasswordField(validators=[Required()])
	Firstname = StringField(validators=[Required()])
	Lastname = StringField(validators=[Required()])
	Email = StringField(validators=[Required()])
	Location = StringField(validators=[Required()])
	Biography = TextField(validators=[Required()])
	photo = FileField('ProfilePhoto', validators=[FileRequired(), FileAllowed('jpg','png','jpeg')])

class LoginForm(FlaskForm):
    Username = StringField('Username', validators=[InputRequired()])




#class UploadForm(FlaskForm):
#  Photo = FileField(validators=[FileRequired(), FileAllowed(["jpg","png","jpeg"])])
#  Description = TextField(validators = [DataRequired()])