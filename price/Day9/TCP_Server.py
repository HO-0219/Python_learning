# TCP서버 - 클라이언트 
# TCP_Server
import socket

# 1. 소켓 생성 (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. IP, PORT 바인딩 (서버 실행할 주소와 포트)
server_socket.bind(("127.0.0.1", 9999))

# 3. 연결 대기 (최대 5명 대기 가능)
server_socket.listen(5)
print("서버 실행 중...")

# 4. 클라이언트 연결 대기
client_socket, addr = server_socket.accept()
print(f"클라이언트 연결됨: {addr}")

# 5. 데이터 송수신
data = client_socket.recv(1024).decode()
print(f"받은 데이터: {data}")

client_socket.sendall("Hello from Server!".encode())

# 6. 소켓 종료
client_socket.close()
server_socket.close()
