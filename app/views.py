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

@app.route('/api/test')
def aws_test():
    data = dict()
    conn = boto.dynamodb.connect_to_region(
        'us-east-1')

    tables = conn.list_tables()
    debug_lines(tables)
    if len(tables) == 0:
        message_table_schema = conn.create_schema(
            hash_key_name='forum_name',
            hash_key_proto_value=str,
            range_key_name='subject',
            range_key_proto_value=str
        )

        table = conn.create_table(
            name='messages',
            schema=message_table_schema,
            read_units=2,
            write_units=2
        )
    return "Table created"

def debug_lines(to_print):
    print "--------------------"
    print "Console debug"
    print to_print
    print "--------------------"