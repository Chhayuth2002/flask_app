from flask import Flask, render_template, request, redirect, Response, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from models import Product, Category, Sale, Customer, Base  
from flask_cors import CORS
app = Flask(__name__)


engine = create_engine("mysql+mysqlconnector://flask:root@localhost/flask")
connection = engine.connect()
Base.metadata.create_all(engine)
import routes
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
