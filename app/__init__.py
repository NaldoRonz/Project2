from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfasa60q0s_ytvctyvrd4xgMY(p\xed_)\xe8\xc9w(\x06\x8e\xf0f(g6g9t\xd2\xba6ges3ojinubvr#s2s-rytturyv5r\xfd\x8c\xda'
app.config['UPLOAD_FOLDER'] = "app/static/uploads"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:RSK4LFEg@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
from app import views, models


