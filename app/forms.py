from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import TextField, FileField, StringField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename


class RegisterForm(FlaskForm):
	Username = StringField(validatiors=[DataRequired])
	Password = PasswordField(validatiors=[DataRequired])
	Firstname = StringField(validatiors=[DataRequired])
	Lastname = StringField(validatiors=[DataRequired])
	Email = StringField(validatiors=[DataRequired])
	Location = StringField(validatiors=[DataRequired])
	Biography = TextField(validators=[DataRequired])




#class UploadForm(FlaskForm):
#  Photo = FileField(validators=[FileRequired(), FileAllowed(["jpg","png","jpeg"])])
#  Description = TextField(validators = [DataRequired()])