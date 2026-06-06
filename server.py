import socket
import threading
import sys

HOST = '127.0.0.1'  
PORT = 65432 

def receive_messages(client_socket):
    """This function runs in a background thread to handle incoming client messages."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message or message.lower() == 'exit':
                print("\n[-] Client disconnected. Press Enter to exit.")
                break
                
            print(f"\n[Client]: {message}")
            print("[You (Server)]: ", end="", flush=True)
            
        except ConnectionResetError:
            print("\n[-] Connection lost unexpectedly.")
            break
        except Exception:
            break
            
    client_socket.close()
    sys.exit()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allows immediate port reuse if you restart the server quickly
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[*] Server is listening on {HOST}:{PORT}...")
    
    try:
        client_socket, client_address = server_socket.accept()
        print(f"[+] Connected to client at: {client_address}")
        print("Type your message and press Enter. Type 'exit' to quit.\n")
        
        # 1. Start background thread to listen for client messages
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()
        
        # 2. Main thread handles ONLY sending server replies
        while True:
            server_reply = input("[You (Server)]: ")
            if not server_reply.strip():
                continue
                
            client_socket.send(server_reply.encode('utf-8'))
            
            if server_reply.lower() == 'exit':
                print("[-] Shutting down connection...")
                break
                
    except Exception as e:
        print(f"[-] Server error: {e}")
    finally:
        server_socket.close()
        print("[*] Server shut down.")

if __name__ == "__main__":
    start_server()