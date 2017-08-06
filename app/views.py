# Bring in the Flask object declared
# in app/__init__.py
from app import app
from flask import render_template, jsonify
import boto
import boto.dynamodb

test = True

# decorate the index function with the
# flask route method. These will be ran
# when the browser goes to these routes 
# of our page
@app.route('/')
@app.route('/index')
def index():
    debug_lines(">>index")
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<user>')
def helloDynamic(user=None):
    return render_template('hello.html', user=user)

def debug_lines(to_print):
    print "--------------------"
    print "Console debug"
    print to_print
    print "--------------------"