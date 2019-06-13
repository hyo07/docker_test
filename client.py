import socket


def __get_myip():
    # 環境によって socket.gethostbyname(socket.gethostname())ではうまくIPアドレスが取れないためこちらを使った
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()[0]


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_socket.connect(('192.168.11.32', 50030))
my_socket.connect((__get_myip(), 50030))
# my_text = 'Hello! This is test message from my sample client!'
my_text = '私が来た！！！！！！！！'
my_socket.sendall(my_text.encode('utf-8'))
