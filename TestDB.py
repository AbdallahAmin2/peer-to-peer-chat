import time
from db import DB 
def stress_test_account_exist(user_count):
    start_time = time.time()
    db = DB()  # Instantiate DB class
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
    db = DB()  # Instantiate DB class
    for i in range(user_count):
        username = f'test_user_{i}'
        password = db.get_password(username)
    total_time = time.time() - start_time
    return total_time

def stress_test_account_online(user_count):
    start_time = time.time()
    db = DB()  # Instantiate DB class
    for i in range(user_count):
        username = f'test_user_{i}'
        account_online = db.is_account_online(username)
    total_time = time.time() - start_time
    return total_time

def stress_test_user_login(user_count):
    start_time = time.time()
    db = DB()  # Instantiate DB class
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
    db = DB()  # Instantiate DB class
    for i in range(user_count):
        username = f'test_user_{i}'
        db.user_logout(username)
    total_time = time.time() - start_time
    return total_time

def stress_test_get_peer_ip_port(user_count):
    start_time = time.time()
    db = DB()  # Instantiate DB class
    for i in range(user_count):
        username = f'test_user_{i}'
        peer_ip_port = db.get_peer_ip_port(username)
    total_time = time.time() - start_time
    return total_time

def stress_test_get_peer_ip_udp_port(user_count):
    start_time = time.time()
    db = DB()  # Instantiate DB class
    for i in range(user_count):
        username = f'test_user_{i}'
        peer_ip_udp_port = db.get_peer_ip_udp_port(username)
    total_time = time.time() - start_time
    return total_time


# Stress testing
account_exist_time = stress_test_account_exist(10000)
register_time = stress_test_register(10000)
get_password_time = stress_test_get_password(10000)
account_online_time = stress_test_account_online(10000)
user_login_time = stress_test_user_login(10000)
user_logout_time = stress_test_user_logout(10000)
get_peer_ip_port_time = stress_test_get_peer_ip_port(10000)
get_peer_ip_udp_port_time = stress_test_get_peer_ip_udp_port(10000)

# Print results
print(f"Account Exist Time: {account_exist_time} seconds")
print(f"Register Time: {register_time} seconds")
print(f"Get Password Time: {get_password_time} seconds")
print(f"Account Online Time: {account_online_time} seconds")
print(f"User Login Time: {user_login_time} seconds")
print(f"User Logout Time: {user_logout_time} seconds")
print(f"Get Peer IP Port Time: {get_peer_ip_port_time} seconds")
print(f"Get Peer IP UDP Port Time: {get_peer_ip_udp_port_time} seconds")


