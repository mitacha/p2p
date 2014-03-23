__author__ = 'Adam'
import socket

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

dict_list = []


def create_peer_list(dictionary_list, hostname, port):
    keys = ['Hostname', 'Port Number']

    entry = [hostname, str(port)]
    dictionary_list.append(dict(zip(keys, entry)))
    return dict_list, keys


def print_dictionary(dictionary_list, keys):
    for item in dictionary_list:
        print(' '.join([item[key] for key in keys]))

while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    dict_list, keys = create_peer_list(dict_list, addr[0], addr[1])
    print_dictionary(dict_list, keys)
    c.send(bytes('Thank you for connecting', "utf-8"))
    c.close()                # Close the connection

