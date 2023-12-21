from flask import Flask, render_template, request, redirect, Response
from sqlalchemy import create_engine, text

app = Flask(__name__)


# Connect to the database
engine = create_engine("mysql+mysqlconnector://flask:root@localhost/flask")
# Test the connection
connection = engine.connect()


@app.route('/')
def hello():
    return 'Hello, World!'
