import socket,threading
import ast
ip_addres=socket.gethostbyname(socket.gethostname())
port=20114

format="utf-8"
session_number=0
session_member=0
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip_addres,port))
mouves=[]
clients_sessions=[]
sessions=[]
def send(conn,msg):
    msg_length=str(len(str(msg)))
    if type(msg)!=str :msg=str(msg) 
    conn.send(msg_length.encode(format))
    
    conn.send(msg.encode(format))
def recv(conn):
    try:
        msg_length=int(conn.recv(32).decode(format))
    except:return "/disconnect"
    msg=conn.recv(msg_length).decode(format)
    return msg


def start():
    global session_number,session_member
    global sessions,clients_sessions
    server.listen()
    print("server listening")

    while True:
        conn,add=server.accept()

        if len(sessions)==0:
            sessions.append([])
            clients_sessions.append([conn])
            conf=recv(conn)
            send(conn,session_member)
            threading.Thread(target=handle,args=(conn,add,session_number,session_member)).start()
            session_member=1
        else:
            for index,session in enumerate(sessions):
                if len(session)==1:
                    session_number=index
                    session_member=1
                    print("one")
                    break
                elif len(session)==0:
                    session_number=index
                    session_member=0
                    print("none")
                    break
                if index==len(sessions)-1 and len(session)!=2:
                    sessions.append([])
                    session_member=0
                    session_number=index
                    print("new_session")
            
            sessions[session_number].append([])
            clients_sessions[session_number].append(conn)
            print(session_member)
            conf=recv(conn)
            send(conn,session_member)
            threading.Thread(target=handle,args=(conn,add,session_number,session_member)).start()
        print(f"new connection from ({add})")

def handle(conn,add,session_index,index_in_session):
    global sessions
    if index_in_session==1:enemy_index=0
    else:enemy_index=1
    while True:
        msg=recv(conn)
        if msg=="/disconnect":
            print(f"disconnected from {add}")
            break
        if msg=="sending_mouve":
            send(conn,"ok")
            start_pos=recv(conn)
            start_pos=ast.literal_eval(start_pos)
            send(conn,"ok")
            end_pos=recv(conn)   
            end_pos=ast.literal_eval(end_pos)     
            try:
                sessions[session_index][index_in_session]=[start_pos,end_pos]
            except :
                sessions[session_index].append([start_pos,end_pos])
            print(sessions)
            send(clients_sessions[session_number][enemy_index],[start_pos,end_pos])
            
    conn.close()

start()
