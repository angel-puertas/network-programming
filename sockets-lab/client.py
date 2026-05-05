import socket 
  
HOST = 'localhost'  # 127.0.0.1 — same machine 
PORT = 65432 
  
try: 
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
     s.connect((HOST, PORT)) 
     print("[CLIENT] Connected to server.") 
     while True: 
         message = input("Enter message (or 'exit'): ") 
         if message.lower() == 'exit': 
             break 
         s.sendall(message.encode()) 
         data = s.recv(1024) 
         if not data: 
             print("[CLIENT] Server closed the connection.") 
             break 
         print(f"[CLIENT] Received: {data.decode()}") 
except ConnectionRefusedError: 
 print("[CLIENT] Could not connect — is the server running?") 
except KeyboardInterrupt: 
 print("\n[CLIENT] Aborted by user.")