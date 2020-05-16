from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import TextField, FileField, StringField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename


class RegisterForm(FlaskForm):
	Username = StringField('Username',validatiors=[DataRequired])
	Password = PasswordField('Password',validatiors=[DataRequired])
	Firstname = StringField('Firstname',validatiors=[DataRequired])
	Lastname = StringField('Lastname',validatiors=[DataRequired])
	Email = StringField('email',validatiors=[DataRequired])
	Location = StringField('location',validatiors=[DataRequired])
	Biography = TextAreaField('Biography',validators=[DataRequired])
  photo = FileField('ProfilePhoto', validators=[FileRequired(), FileAllowed('jpg','png','jpeg')])




#class UploadForm(FlaskForm):
#  Photo = FileField(validators=[FileRequired(), FileAllowed(["jpg","png","jpeg"])])
#  Description = TextField(validators = [DataRequired()])