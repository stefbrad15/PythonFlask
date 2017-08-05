from flask import Flask

app = Flask(__name__, static_path='/static')


# It's import this after creating app
# so that views can then import app
from app import views
