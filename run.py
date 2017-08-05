#!/usr/bin/env python

# Look for a folder named app with a variable named app
# and provide a reference of this object
from app import app

# In __init__ py app is an instance of the Flask object which
# has a run method that will start the web application
app.run(debug=True)