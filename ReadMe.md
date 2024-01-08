 # Peer-to-Peer Chat Application with Instruction Tuning and RLHF

This repository contains the code for a peer-to-peer chat application that utilizes instruction tuning and reinforcement learning from human feedback (RLHF) to provide intelligent and user-friendly features. The application allows users to create accounts, log in, search for other users, send one-to-one messages, and participate in chat rooms.

## Prerequisites

To run this application, you will need the following:

* Python 3.8 or later
* The `socket` module
* The `threading` module
* The `colorama` module

## Installation

To install the required modules, run the following command in your terminal:

```
pip install -r requirements.txt
```

## Usage

To start the application, run the following command in your terminal:

```
python main.py
```

You will be prompted to enter the IP address of the registry server. The default IP address is `localhost`.

Once you have entered the IP address of the registry server, you will be prompted to create an account or log in.

### Creating an Account

To create an account, enter the following command:

```
JOIN username password
```

For example:

```
JOIN alice password123
```

### Logging In

To log in, enter the following command:

```
LOGIN username password peerServerPort
```

For example:

```
LOGIN alice password123 5000
```

### Searching for Users

To search for a user, enter the following command:

```
SEARCH username
```

For example:

```
SEARCH bob
```

### Sending One-to-One Messages

To send a one-to-one message, enter the following command:

```
ONE_TO_ONE_CHAT_MESSAGE username message
```

For example:

```
ONE_TO_ONE_CHAT_MESSAGE bob Hello, how are you?
```

### Participating in Chat Rooms

To participate in a chat room, enter the following command:

```
JOIN-CHAT chatroomName
```

For example:

```
JOIN-CHAT general
```

## Code Overview

The code for the peer-to-peer chat application is organized into three main classes:

* `PeerServer`
* `PeerClient`
* `peerMain`

### PeerServer Class

The `PeerServer`
