# importamos el paquete de sockets
import socket

# Creamos un seridor de sockets UDP
# que con el servidor
# AF_INET       -> socket de internet
# SOCK_DGRAM    -> socket de tipo UDP, es decir, sin conexión
#                  entre el servidor y el cliente. Se mandaran
#                  mensajes independientes
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Tenemos que vincular el servidor a una IP y un puerto
# en este caso se hara la practica de forma local, 
# ejecutando el cliente y servidor en la misma maquina
server.bind(("localhost", 9000));


# Podemos usar dos métodos para recibir mensajes de un cliente
# recv      ->  este método solo devuelve el mensaje del cliente, 
#               Pero no devuelve la dirección, por lo que no 
#               podemos contestarle al cliente.
#
# recvfrom  ->  este método devuelve la dirección y el mensaje

message, address = server.recvfrom(1024)
print(message.decode("utf-8"))

# Aqui le enviamos un mensaje el cliente, con el address
# que obtuvimos de su mensaje

server.sendto("Hello client".encode("utf-8"), address)