from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
#cors will throw error is obj from other servers (front end = diff server from backend) will contack our db
app = Flask (__name__)
CORS(app)
#the above 2 lines stop the CORS error
#initialize DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
#Make sure all the modifications made are not tracked. May be changed later
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#creating an obj of SQLAlchemy so that using this object we may pass our py code to manipulate DB
db = SQLAlchemy(app)

