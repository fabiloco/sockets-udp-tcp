# importamos el paquete de sockets
import socket

# Creamos un servidor de sockets TCP
# AF_INET       -> socket de internet - tipo de direccion
# SOCK_STREAM   -> socket de tipo tcp, es decir, con conexión
#                  entre el servidor y el cliente

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tenemos que vincular el servidor a una IP y un puerto
# en este caso se hara la practica de forma local, 
# ejecutando el cliente y servidor en la misma maquina
server.bind(("localhost", 9000))

# Ponemos el servidor en escucha de nuevas solicitudes
server.listen()

while True:
    # Este método espera por un conexión, y una vez sucede, 
    # devuelve el servidor del cliente que se intenta 
    # conectar y su dirección
    client, address = server.accept()
    print(f"Connected to {address}")
    print(client.recv(1024).decode("utf-8"))
    client.send("Hello client!".encode("utf-8"))
    
    print(client.recv(1024).decode("utf-8"))
    client.send("Bye".encode("utf-8"))

    # Si queremos dejar de recibir mensajes en TCP, debemos
    # cerrar la conexión explicitamente
    client.close()
