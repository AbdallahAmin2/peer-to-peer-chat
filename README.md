 # Peer-to-Peer Chat Application

This is a peer-to-peer chat application that allows users to create accounts, log in, and chat with each other. The application uses a registry server to keep track of online users and their IP addresses. Each peer runs a server and a client. The server listens for incoming connections from other peers, and the client connects to other peers' servers.

## Getting Started

To run the application, you will need to install Python 3 and the following libraries:

* socket
* threading
* select
* logging
* colorama

Once you have installed the required libraries, you can clone the repository and run the following command:

```
python peer.py
```

This will start the peer-to-peer chat application.

## User Interface

The user interface of the application is a command-line menu. The following options are available:

* Create account
* Login
* Logout
* Search for a user
* Start a chat
* Create a chat room
* Join a chat room
* List online users
* List chat rooms

## Creating an Account

To create an account, select the "Create account" option from the menu. You will be prompted to enter a username and password. The username must be unique, and the password must be at least 8 characters long.

## Logging In

To log in, select the "Login" option from the menu. You will be prompted to enter your username and password. If the username and password are correct, you will be logged in and the peer server will start.

## Logging Out

To log out, select the "Logout" option from the menu. You will be logged out and the peer server will stop.

## Searching for a User

To search for a user, select the "Search for a user" option from the menu. You will be prompted to enter the username of the user you want to search for. If the user is found, their IP address will be displayed.

## Starting a Chat

To start a chat, select the "Start a chat" option from the menu. You will be prompted to enter the username of the user you want to chat with. If the user is found and online, a chat window will open.

## Creating a Chat Room

To create a chat room, select the "Create a chat room" option from the menu. You will be prompted to enter a name for the chat room. If the

