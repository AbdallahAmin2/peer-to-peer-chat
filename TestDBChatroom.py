import unittest
from ChatRoomsDB import DB

class TestDBChatRoom(unittest.TestCase):

    def setUp(self):
        # Initialize DB for testing
        self.db_access = DB()

    def tearDown(self):
        # Clean up any resources after tests are run
        # For example, delete test users created during testing
        self.db_access.db.peer.delete_many({'username': {'$in': ['test_user', 'new_user']}})
        self.db_access.db.online_peers.delete_many({'username': {'$in': ['test_user', 'new_user']}})
        self.db_access.db.rooms.delete_many({'room_name': {'$in': ['test_room', 'new_room']}})

    def test_get_chat_rooms(self):
        # Test retrieving chat rooms when there are existing rooms
        self.db_access.create_room('test_room')
        self.db_access.create_room('new_room')
        expected_rooms = ['test_room', 'new_room']
        self.assertCountEqual(self.db_access.get_chat_rooms(), expected_rooms)

        # Test retrieving chat rooms when there are no rooms
        self.db_access.delete_room('test_room')
        self.db_access.delete_room('new_room')
        self.assertEqual(self.db_access.get_chat_rooms(), [])

    def test_get_rooms_for_user(self):
        # Test checking chat room existence when the room exists
        self.db_access.create_room('test_room')
        self.assertTrue(self.db_access.get_rooms_for_user('test_room'))

        # Test checking chat room existence when the room doesn't exist
        self.assertFalse(self.db_access.get_rooms_for_user('non_existing_room'))

    def test_join_room(self):
        # Test joining an existing chat room
        self.db_access.create_user('test_user', 'password', "")
        self.db_access.create_room('test_room')
        self.assertTrue(self.db_access.join_room('test_room', 'test_user'))

        # Test joining a non-existing chat room
        self.assertFalse(self.db_access.join_room('non_existing_room', 'test_user'))

    def test_create_room(self):
        # Test creating a new chat room
        self.assertTrue(self.db_access.create_room('new_room'))

        # Test creating an existing chat room
        self.assertFalse(self.db_access.create_room('new_room'))

    def test_get_rooms_for_user(self):
        # Test checking users in chatroom
        self.db_access.create_room('test_room')
        self.assertTrue(self.db_access.get_rooms_for_user('test_room'))

        # Test checking there is no users in chatroom
        self.assertFalse(self.db_access.get_rooms_for_user('non_existing_room'))

if __name__ == '__main__':
    unittest.main()


