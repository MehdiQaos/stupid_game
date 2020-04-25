# import threading
# import socket
#
# server = '192.168.1.12'
# port = 8881
#
#
# def threaded_client(conn: socket.socket):
#     conn.send(str.encode('connected'))
#     reply = ""
#
#     while True:
#         try:
#             data = conn.recv(2048)
#             replay = data.decode('utf-8')
#
#             if not data:
#                 print('Disconnected')
#                 break
#             else:
#                 print(f'Received: {replay}')
#                 print(f'sending: {replay.upper()}')
#             conn.sendall(replay.upper().encode())
#         except:
#             break
#
#     print('lost connection')
#     conn.close()
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     s.bind((server, port))
# except socket.error as e:
#     print(f'error binding: {e}')
#
# s.listen(2)
# print('waiting for a connection server started')
#
# while True:
#     conn, addr = s.accept()
#     print(f'connected to: {addr}')
#     t = threading.Thread(target=threaded_client, args=(conn,))
#     t.start()







import socket
import _thread
import pickle

SERVER = '192.168.1.14'
PORT = 8005
ADDRESS = SERVER, PORT
positions = [(0,0), (100,100)]


def threaded_client(conn, player_id):
    conn.send(pickle.dumps(positions[player_id]))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            if data:
                positions[player_id] = data
                if player_id == 0:
                    conn.send(pickle.dumps(positions[1]))
                else:
                    conn.send(pickle.dumps(positions[0]))

            else:
                print(f'disconnecting')
                conn.close()
                break
        except socket.error as e:
            print(f'ERROR: {e}')
    print('DISCONNECTED')


sock = socket.socket()
sock.bind(ADDRESS)
sock.listen(2)
print(f'Server started on {ADDRESS} waiting for a connection...')

player_id = 0
while True:
    conn, addr = sock.accept()
    print(f'connected to {addr}')
    _thread.start_new_thread(threaded_client, (conn, player_id))
    player_id += 1
























