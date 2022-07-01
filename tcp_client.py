# importamos el paquete de sockets
import socket

# Creamos un cliente de sockets TCP de la misma manera
# que con el servidor
# AF_INET       -> socket de internet
# SOCK_STREAM   -> socket de tipo tcp, es decir, con conexión
#                  entre el servidor y el cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos el cliente a la misma dirección a la que
# enlazamos el servidor
client.connect(("localhost", 9000))

client.send("Hello server".encode("utf-8"))
print(client.recv(1024).decode("utf-8"))

client.send("Bye".encode("utf-8"))
print(client.recv(1024).decode("utf-8"))