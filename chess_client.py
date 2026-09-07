import socket
import threading,ast
ip_address="192.168.1.16"
port=20114
format="utf-8"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

running=False


def send(msg):
    msg=str(msg)
    msg_length=str(len(str(msg)))
    client.send(msg_length.encode(format))
    
    client.send(msg.encode(format))
def recv():
    
    msg_length=int(client.recv(1024).decode(format))
    
    msg=client.recv(msg_length).decode(format)
    return msg

def start():
    global running
    client.connect((ip_address,port))
    # threading.Thread(target=handle).start()
    running=True
    print("connected")
    # while running:
    #     msg=str(input(""))
    #     if running :
    #         send(msg)
    #     if msg=="/disconnect":break
def handle():
    global running
    while True:
        msg=recv()
        if msg=="/disconnect":break
        print(msg)
    running=False
    client.close()

def send_move(from_,to_):
    send("sending_position")
    send(from_)
    send(to_)

def receive_position():
    mouve=recv()
    return ast.literal_eval(mouve)


