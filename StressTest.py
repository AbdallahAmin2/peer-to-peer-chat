import time
from colorama import Fore
from peer import peerMain
from peer import PeerServer
from peer import PeerClient
from peer import UDP_Reciever, peerMain 
from db import DB
from ChatRoomsDB import Chatroomsdb

# Stress testing for peerMain class
def stress_test_create_account(user_count):
    start_time = time.time()
    main = peerMain()
    for i in range(user_count):
        username = f'test_user_{i}'
        password = f'test_password_{i}'
        main.createAccount(username, password)
    total_time = time.time() - start_time
    return total_time

def stress_test_login(user_count):
    start_time = time.time()
    main = peerMain()
    for i in range(user_count):
        username = f'test_user_{i}'
        password = f'test_password_{i}'
        peer_server_port = 12340 + i
        udp_port = 23450 + i
        status = main.login(username, password, peer_server_port, udp_port)
    total_time = time.time() - start_time
    return total_time

def stress_test_logout(user_count):
    start_time = time.time()
    main = peerMain()
    for i in range(user_count):
        main.logout(1)
    total_time = time.time() - start_time
    return total_time

# Stress testing for DB class
def stress_test_account_exist(user_count):
    start_time = time.time()
    db = DB()
    for i in range(user_count):
        username = f'test_user_{i}'
        account_exist = db.is_account_exist(username)
    total_time = time.time() - start_time
    return total_time

def stress_test_register(user_count):
    start_time = time.time()
    db = DB()
    for i in range(user_count):
        username = f'test_user_{i}'
        password = f'test_password_{i}'
        db.register(username, password)
    total_time = time.time() - start_time
    return total_time

def stress_test_get_password(user_count):
    start_time = time.time()
    db = DB()
    for i in range(user_count):
        username = f'test_user_{i}'
        password = db.get_password(username)
    total_time = time.time() - start_time
    return total_time

def stress_test_account_online(user_count):
    start_time = time.time()
    db = DB()
    for i in range(user_count):
        username = f'test_user_{i}'
        account_online = db.is_account_online(username)
    total_time = time.time() - start_time
    return total_time

def stress_test_user_login(user_count):
    start_time = time.time()
    db = DB()
    for i in range(user_count):
        username = f'test_user_{i}'
        ip = '127.0.0.1'
        tcp_port = 12340 + i
        udp_port = 23450 + i
        db.user_login(username, ip, tcp_port, udp_port)
    total_time = time.time() - start_time
    return total_time

def stress_test_user_logout(user_count):
    start_time = time.time()
    db = DB()
    for i in range(user_count):
        username = f'test_user_{i}'
        db.user_logout(username)
    total_time = time.time() - start_time
    return total_time

def stress_test_get_peer_ip_port(user_count):
    start_time = time.time()
    db = DB()
    for i in range(user_count):
        username = f'test_user_{i}'
        peer_ip_port = db.get_peer_ip_port(username)
    total_time = time.time() - start_time
    return total_time

def stress_test_get_peer_ip_udp_port(user_count):
    start_time = time.time()
    db = DB()
    for i in range(user_count):
        username = f'test_user_{i}'
        peer_ip_udp_port = db.get_peer_ip_udp_port(username)
    total_time = time.time() - start_time
    return total_time

# Stress testing for Chatroomsdb class
def stress_test_create_room(room_count):
    start_time = time.time()
    chat_db = Chatroomsdb()
    for i in range(room_count):
        room_name = f'test_room_{i}'
        chat_db.create_room(room_name)
    total_time = time.time() - start_time
    return total_time

def stress_test_join_room(room_count, user_count):
    start_time = time.time()
    chat_db = Chatroomsdb()
    for i in range(room_count):
        room_id = i + 1
        for j in range(user_count):
            username = f'test_user_{j}'
            chat_db.join_room(room_id, username)
    total_time = time.time() - start_time
    return total_time

def stress_test_user_leave_room(room_count, user_count):
    start_time = time.time()
    chat_db = Chatroomsdb()
    for i in range(room_count):
        room_id = i + 1
        for j in range(user_count):
            username = f'test_user_{j}'
            chat_db.user_leave_room(room_id, username)
    total_time = time.time() - start_time
    return total_time

# Stress testing
# For peerMain class
create_account_time = stress_test_create_account(1000)
login_time = stress_test_login(1000)
logout_time = stress_test_logout(1000)

# For DB class
account_exist_time = stress_test_account_exist(1000)
register_time = stress_test_register(1000)
get_password_time = stress_test_get_password(1000)
account_online_time = stress_test_account_online(1000)
user_login_time = stress_test_user_login(1000)
user_logout_time = stress_test_user_logout(1000)
get_peer_ip_port_time = stress_test_get_peer_ip_port(1000)
get_peer_ip_udp_port_time = stress_test_get_peer_ip_udp_port(1000)

# For Chatroomsdb class
create_room_time = stress_test_create_room(100)
join_room_time = stress_test_join_room(100, 10)
user_leave_room_time = stress_test_user_leave_room(100, 10)

# Print results for peerMain class
print(f"{Fore.GREEN}PeerMain Class Stress Testing{Fore.RESET}")
print(f"Create Account Time: {create_account_time} seconds")
print(f"Login Time: {login_time} seconds")
print(f"Logout Time: {logout_time} seconds")

# Print results for DB class
print(f"\n{Fore.BLUE}DB Class Stress Testing{Fore.RESET}")
print(f"Account Exist Time: {account_exist_time} seconds")
print(f"Register Time: {register_time} seconds")
print(f"Get Password Time: {get_password_time} seconds")
print(f"Account Online Time: {account_online_time} seconds")
print(f"User Login Time: {user_login_time} seconds")
print(f"User Logout Time: {user_logout_time} seconds")
print(f"Get Peer IP Port Time: {get_peer_ip_port_time} seconds")
print(f"Get Peer IP UDP Port Time: {get_peer_ip_udp_port_time} seconds")

# Print results for Chatroomsdb class
print(f"\n{Fore.YELLOW}Chatroomsdb Class Stress Testing{Fore.RESET}")
print(f"Create Room Time: {create_room_time} seconds")
print(f"Join Room Time: {join_room_time} seconds")
print(f"User Leave Room Time: {user_leave_room_time} seconds")


