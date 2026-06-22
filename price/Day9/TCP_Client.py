# TCP_Client 
import socket

# 1. 소켓 생성 (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 서버에 연결
client_socket.connect(("127.0.0.1", 9999))

# 3. 데이터 송수신
client_socket.sendall("Hello Server!".encode())

data = client_socket.recv(1024).decode()
print(f"서버 응답: {data}")

# 4. 소켓 종료
client_socket.close()
