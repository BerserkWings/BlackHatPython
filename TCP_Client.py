"""Utilizaremos la libreria Socket para crear un cliente TCP, con esto mandaremos algo de data y la recibiremos, con el
fin de coprobar si nuestro cliente TCP funciona"""

import socket

"""
target_host = "google.com" # Puedes cambiarlo a cualquier host
target_port = 80
"""

# Variables que sirven en el servidor TCP
target_host = '127.0.0.1'
target_port = 9998

# Creando el objeto Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando el cliente
client.connect((target_host, target_port))

# Enviando algo de data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") # La data se envia en bytes

# Recibiendo la data
response = client.recv(1024)

# Imprimiento la data y cerrando el cliente
print(response.decode())
client.close()

"""
Explicando algunos parametros:
* AF_INET = indica que usaremos eL estandar de dirección IPv4 o el hostname
* SOCK_STREAM = indica que la vairable sera el cliente TCP. 

Si ejecutamos el programa, nos regresara un POST como en BurpSuite, aunque no se vera bien.
"""
