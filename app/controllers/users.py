from app import app
from app.helpers import user_helpers as u_helper
from app.helpers import DynamoInterface
from flask import jsonify, request

@app.route("/api/user", methods=['GET'])
def get_user():
    username = request.args['username']
    password = request.args['password']
    encrypted_pass = u_helper.encrypt_password(password)
    i_dynamo = DynamoInterface()

    user_table = i_dynamo.get_table('users')
    try:
        user = user_table.get_item(
            username=username,
            password=encrypted_pass
        )
        return jsonify(dict(user))
    except Exception as e:
        return str(e)
    
@app.route('/api/users', methods=['GET'])
def get_all_users():
    i_dynamo = DynamoInterface()
    tables = i_dynamo.list_tables()
    app.logger.debug(tables)

    if "users" not in tables:
        users = u_helper.create_user_table(i_dynamo, app.logger)
        return jsonify(users)
    else:        
        attributes = (
            'username', 
            'first_name', 
            'last_name', 
            'account_type'
            )
        users = i_dynamo.get_all_items("users", attributes)
        return jsonify(users)
