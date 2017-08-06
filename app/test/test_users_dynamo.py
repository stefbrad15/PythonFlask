import pytest
from app.helpers import DynamoInterface
from app.helpers import user_helpers

@pytest.fixture
def db():
    return DynamoInterface()

class TestUserDynamoTable(object):
    def test_user_table_exists(self, db):       
        tables = db.list_tables()
        assert 'users' in tables

    def test_get_all_user(self, db):
        users = db.get_all_items('users')
        assert len(users) != 0

    def test_get_user(self, db):
        table = db.get_table('users')
        password = user_helpers.encrypt_password('JohnPass123')
        user = table.get_item(
            username='johndoe',password=password
        )
        assert user['first_name'] == 'John'

    def test_new_user(self, db):
        table = db.get_table('users')
        new_user = {
            'username' : 'testuser',
            'password' : 'testpass',
            'first_name' : 'test'
        }
        status = table.put_item(new_user)
        
        assert status

    def test_update(self, db):
        table = db.get_table('users')
        user = table.get_item(
            username='testuser',password='testpass'
        )
        assert user['first_name'] == 'test'

        user['first_name'] = "Jim"
        assert user.save()

    def test_del_user(self, db):
        table = db.get_table('users')
        user = table.get_item(
            username='testuser',password='testpass'
        )
        # Assert previous update
        assert user['first_name'] == "Jim"
        assert user.delete()