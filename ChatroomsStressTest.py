import time
from ChatRoomsDB import Chatroomsdb 

def stress_test_create_room(room_count):
    start_time = time.time()
    chat_db = Chatroomsdb()  # Instantiate Chatroomsdb
    for i in range(room_count):
        room_name = f'test_room_{i}'
        chat_db.create_room(room_name)
    total_time = time.time() - start_time
    return total_time

def stress_test_join_leave_room(room_count, user_count):
    start_time = time.time()
    chat_db = Chatroomsdb()  # Instantiate Chatroomsdb
    for i in range(room_count):
        room_id = i + 1
        for j in range(user_count):
            username = f'test_user_{j}'
            chat_db.join_room(room_id, username)
        for j in range(user_count):
            username = f'test_user_{j}'
            chat_db.user_leave_room(room_id, username)
    total_time = time.time() - start_time
    return total_time

def stress_test_get_available_rooms():
    start_time = time.time()
    chat_db = Chatroomsdb()  # Instantiate Chatroomsdb
    available_rooms = chat_db.get_available_rooms()
    total_time = time.time() - start_time
    return total_time

def stress_test_get_users_in_room(room_count):
    start_time = time.time()
    chat_db = Chatroomsdb()  # Instantiate Chatroomsdb
    for i in range(room_count):
        room_id = i + 1
        users_in_room = chat_db.get_users_in_room(room_id)
    total_time = time.time() - start_time
    return total_time


# Stress testing
create_room_time = stress_test_create_room(100)
join_leave_room_time = stress_test_join_leave_room(100, 10)
get_available_rooms_time = stress_test_get_available_rooms()
get_users_in_room_time = stress_test_get_users_in_room(100)

# Print results
print(f"Create Room Time: {create_room_time} seconds")
print(f"Join and Leave Room Time: {join_leave_room_time} seconds")
print(f"Get Available Rooms Time: {get_available_rooms_time} seconds")
print(f"Get Users in Room Time: {get_users_in_room_time} seconds")
