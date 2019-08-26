import socket
import argparse
import time
from threading import Thread

from acceptor import listenForClients

# Do argument work
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--port", default=6060)
args = ap.parse_args()

# Deal with type conversions
args.port = int(args.port)

# Start up master socket
sessions = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", args.port))
sock.listen(1)

# Listen for clients in a thread
print("Started listener")
client_listener = Thread(target=listenForClients, args=[sock])
client_listener.start()

while True:
    time.sleep(1)