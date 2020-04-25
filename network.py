# import socket
#
#
# class Network:
#     def __init__(self):
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.server = '192.168.1.12'
#         self.port = 8881
#         self.addr = (self.server, self.port)
#         self.pos = self.connect()
#
#     def connect(self):
#         try:
#             self.client.connect(self.addr)
#             return self.client.recv(2048).decode()
#         except:
#             pass
#
#     def send(self, data):
#         try:
#             self.client.send(str.encode(data))
#             return self.client.recv(2048).decode()
#         except socket.error as e:
#             print(e)
#
#
# if __name__ == '__main__':
#     n = Network()
#     print(n.send('hssik'))
#     print(n.send('piq'))


















import socket
import pickle

SERVER = '192.168.1.14'
PORT = 8005


def str_tuple(s):
    temp = s.split(',')
    return int(temp[0]), int(temp[1])


def tuple_str(t):
    return ','.join(map(str, t))


class Network:
    def __init__(self):
        self.client = socket.socket()
        self.SERVER = SERVER
        self.PORT = PORT
        self.ADDR = self.SERVER, self.PORT
        self.pos = self.connect()

    def get_pos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.ADDR)
            data = self.client.recv(2048)
            return pickle.loads(data)
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)



















