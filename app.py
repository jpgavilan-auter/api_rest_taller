from flask import Flask,jsonify,request, redirect, url_for, flash,send_file
import shutil
from zipfile import ZipFile
import json
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt, get_jwt_identity, set_access_cookies, unset_jwt_cookies, decode_token
import bcrypt
from datetime import timedelta,datetime,timezone
import os
from sqlalchemy import desc, text, distinct
import urllib
import time
import jwt
from models import db,users

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@server/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=60)
jwt = JWTManager(app)