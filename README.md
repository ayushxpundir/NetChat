# NetChat 

A lightweight, Command-Line Interface (CLI) based chat application built using Python's native networking capabilities.



## Project Overview

NetChat follows a classic **Client-Server architecture**. The server acts as a centralized host that binds to a specific local port and listens for incoming connections, while the client connects to the host to facilitate real-time message exchange over TCP.

### Key Concepts Implemented:
* **Networking:** TCP Sockets (`socket.SOCK_STREAM`), IPv4 Addressing (`AF_INET`), Data Serialization/Deserialization (`encode`/`decode` via UTF-8).
* **Version Control:** Feature branching, local repository initialization, staging, committing, and remote repository pushing via Git.



## Getting Started

### Prerequisites
* **Python 3.x** installed on your system.
* **Git** configured locally.

### Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ayush9-prog/NetChat.git
   cd NetChat
   ```

2. **Verify your local files:** Ensure both `server.py` and `client.py` are present in your root directory.


## How to Run the Application

To test the application locally, you will need to open **two separate terminal windows or tabs** to run the host and guest components simultaneously.

### Step 1: Fire up the Server

In your first terminal, execute the server script. This script initializes the port configuration and enters a listening state.

```bash
python server.py

```

*Expected output:* `[*] Server is listening on 127.0.0.1:65432...`

### Step 2: Launch the Client

In your second terminal, execute the client script to establish the network socket connection to the active server.

```bash
python client.py

```

*Expected output:* `[+] Successfully connected to the server at 127.0.0.1:65432`

### Step 3: Chat Away!

* Type a message in the Client terminal and press **Enter**.
* Watch the Server terminal log the text in real-time.
* Type `exit` in the client terminal to safely teardown the TCP connection and free up the network port.


