from email.base64mime import header_length
import bcrypt
from bson import Binary
from pymongo import MongoClient

# Includes database operations
class DB:


    # db initializations
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['p2p-chat']


    # checks if an account with the username exists
    def is_account_exist(self, username):
        if len(list(self.db.accounts.find({'username': username})))> 0:
            return True
        else:
            return False
    

    # registers a user
    def register(self, username, password):
        account = {
            "username": username,
            "password": password
        }
        self.db.accounts.insert_one(account)


    # retrieves the password for a given username
    def get_password(self, username):
        return self.db.accounts.find_one({"username": username})["password"]


    # checks if an account with the username online
    def is_account_online(self, username):
        if len(list(self.db.online_peers.find({"username": username}))) > 0:
            return True
        else:
            return False

    def login(self, username, password):
        # Retrieve the stored hashed password and salt from MongoDB
        user_data = self.db.accounts.find_one({"username": username})
        
        if user_data:
            stored_hashed_password = Binary(user_data.get("password"))
            stored_salt = Binary(user_data.get("password_salt"))

            # Hash the entered password with the retrieved salt
            entered_hashed_password = bcrypt.hashpw(password.encode('utf-8'), stored_salt)

            if entered_hashed_password == stored_hashed_password:
                # Send login details to the server (you might need to adjust this based on your specific implementation)
                username_header_login = f'{len(username):<{header_length}}'.encode('utf-8')
                username_text = username.encode('utf-8')
                client_socket.send(username_header_login + username_text)

                password_header_login = f'{len(password):<{header_length}}'.encode('utf-8')
                password_text = password.encode('utf-8')
                client_socket.send(password_header_login + password_text)

                client_socket.send('login'.encode('utf-8'))
                return True
            else:
                print('Invalid password!')
                return False
        else:
            print('Invalid username or password!')
            return False
    # logs in the user
    def user_login(self, username, ip, port):
        online_peer = {
            "username": username,
            "ip": ip,
            "port": port
        }
        self.db.online_peers.insert_one(online_peer)
    

    # logs out the user 
    def user_logout(self, username):
        self.db.online_peers.remove({"username": username})
    

    # retrieves the ip address and the port number of the username
    def get_peer_ip_port(self, username):
        res = self.db.online_peers.find_one({"username": username})
        return (res["ip"], res["port"])