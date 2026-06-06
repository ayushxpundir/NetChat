import socket
import threading
import sys

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

def receive_messages(client_socket):
    """This function runs in a background thread to handle incoming messages."""
    while True:
        try:
            server_reply = client_socket.recv(1024).decode('utf-8')
            
            if not server_reply or server_reply.lower() == 'exit':
                print("\n[-] Server ended the chat session. Press Enter to exit.")
                break
                
            print(f"\n[Server]: {server_reply}")
            print("[You]: ", end="", flush=True)
            
        except Exception:
            print("\n[-] Connection to server lost.")
            break
            
    client_socket.close()
    sys.exit()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"[+] Successfully connected to the server at {SERVER_HOST}:{SERVER_PORT}")
        print("Type your message and press Enter. Type 'exit' to quit.\n")
        
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True  
        receive_thread.start()
        
        while True:
            user_message = input("[You]: ")
            
            # Guard Clause: Ignore empty inputs or pure spaces
            if not user_message.strip():
                continue
                
            client_socket.send(user_message.encode('utf-8'))
            
            if user_message.lower() == 'exit':
                print("[-] Disconnecting...")
                break
                
    except ConnectionRefusedError:
        print("[-] Could not connect to the server. Is server.py running?")
    finally:
        client_socket.close()
        print("[*] Client closed.")

if __name__ == "__main__":
    start_client()