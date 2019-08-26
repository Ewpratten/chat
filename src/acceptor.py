import socket
from threading import Thread
from messages import greeting
from session import Session

sessions = []

def notifyAll(msg, ses):
    for session in sessions:
        if session != ses:
            session.send(f"<{ses.username}> {msg}")

def svrNotifyAll(msg, ses):
    for session in sessions:
        if session != ses:
            session.send(f"<server> {msg}")

def handleClient(conn, addr):
    conn.send(greeting.encode())

    conn.send(b"The server needs some information about you\nbefore you join.\n")
    conn.send(b"Pick a username> ")

    session = Session()

    data = conn.recv(1024)
    if not data:
        conn.send(b"\nThat is not a valid username. Try again\n")
        conn.close()
    
    session.username = data.decode().strip()
    session.conn = conn
    
    session.send(f"\n<server> Hello {session.username}! Welcome to the chatroom.")

    sessions.append(session)
    svrNotifyAll(f"{session.username} has joined.", session)

    while True:
        data = conn.recv(4096)
        if not data:
            continue
        
        notifyAll(data.decode().strip(), session)



    
def listenForClients(sock: socket.socket):
    while True:
        conn, addr = sock.accept()

        print(f"Accepting {addr}")

        # Spin off a thread to handle the client
        client_thread = Thread(target=handleClient, args=[conn, addr])
        client_thread.start()


