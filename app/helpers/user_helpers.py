import hashlib
import binascii
import time

def create_user_table(dynamo_interface, logger=None):
    """
    Takes a boto.dynamodb.conn object and creates
    a users table on it.

    We want to do this programatically so we can easily
    create this table across different domain and realms
    """
    throughput = {
        'read' : 2,
        'write' : 2
    } 
    table = dynamo_interface.create_table(
        'users', 
        'username', 
        'password', 
        throughput)
    
    time.sleep(10) # give aws time to make the table
    users = seed_user_table(table)

    if logger:
        logger.debug(table)

    return users
    

def seed_user_table(table):
    user_array = list()
    user1 = {
        'username' : 'johndoe',
        'first_name' : 'John',
        'last_name' : 'Doe',
        'account_type' : 'admin_user',
        'password' : encrypt_password("JohnPass123")
    }

    user2 = {
        'username' : 'janedoe',
        'first_name' : 'Jane',
        'last_name' : 'Doe',
        'account_type' : 'standard_user',
        'password' : encrypt_password("JanePass123")
    }
    # check put success
    if table.put_item(user1):
        user_array.append(user1)
        if table.put_item(user2):
            user_array.append(user2)
    
    return user_array


def encrypt_password(password):
    """
    Encrypt and salt the provided password using sha256
    """
    # derived_key
    dk = hashlib.pbkdf2_hmac('sha256', password, "hello_flask", 100007)
    return binascii.hexlify(dk)