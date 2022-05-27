import pymysql
from flask import Flask
from config import *
from flask_sqlalchemy import SQLAlchemy

"""
这里是启动数据库前置操作
"""

# mysql数据库
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
