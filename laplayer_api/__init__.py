from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, send_file

DB_URL = ""

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)
