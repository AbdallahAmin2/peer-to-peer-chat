import unittest
from db import DB

class TestDB(unittest.TestCase):

    def setUp(self):
        # Initialize DB for testing
        self.db_access = DB()

    def tearDown(self):
        # Clean up any resources after tests are run
        # For example, delete test users created during testing
        self.db_access.db.peer.delete_many({'username': {'$in': ['test_user', 'new_user']}})
        self.db_access.db.online_peers.delete_many({'username': {'$in': ['test_user', 'new_user']}})

    def test_user_exists(self):
        # Test user existence when user exists
        self.assertTrue(self.db_access.register('test_user', 'password', ""))
        self.assertTrue(self.db_access.is_account_exist('test_user'))

        # Test user existence when user doesn't exist
        self.assertFalse(self.db_access.is_account_exist('non_existing_user'))

    def test_register(self):
        # Test creating a new user
        self.assertTrue(self.db_access.register('new_user', 'password', ""))

        # Test creating an existing user
        self.assertFalse(self.db_access.register('new_user', 'password', ""))

    def test_get_password(self):
        # Test retrieving password for an existing user
        self.db_access.register('new_user', 'password', "")
        self.assertEqual(self.db_access.get_password('new_user'), 'password')

        # Test retrieving password for a non-existing user
        self.assertIsNone(self.db_access.get_password('non_existing_user'))

    def test_user_status(self):
        # Test when user is online
        self.db_access.online_peers('test_user', 8080, '127.0.0.1')
        self.assertTrue(self.db_access.is_account_online('test_user'))

        # Test when user is offline
        self.db_access.set_user_offline('test_user')
        self.assertFalse(self.db_access.is_account_online('test_user'))

    def test_get_peer_ip_udp_port(self):
        # Test retrieving IP for an existing user
        self.db_access.online_peers('test_user', 8080, '127.0.0.1')
        self.assertEqual(self.db_access.get_peer_ip_port('test_user'), '127.0.0.1')

        # Test retrieving IP for a non-existing user
        self.assertIsNone(self.db_access.get_peer_ip_port('non_existing_user'))
    
    def test_get_peer_ip_port(self):
        # Test retrieving IP for an existing user
        self.db_access.online_peers('test_user', 8080, '127.0.0.1')
        self.assertEqual(self.db_access.get_peer_ip_port('test_user'), '127.0.0.1')

        # Test retrieving IP for a non-existing user
        self.assertIsNone(self.db_access.get_peer_ip_port('non_existing_user'))


if __name__ == '__main__':
    unittest.main()


