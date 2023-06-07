"""Con la misma libreria Socket, crearemos un cliente UDP"""

import socket

target_host = "127.0.0.1"
target_port = 9997

# Creando el objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviando algo de data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# Recibiendo la data
data, addr = client.recvfrom(4096)

# Imprimiendo data y cerrando cliente
print(data.decode())
client.close()

"""
Explicando algunos parametros:
* AF_INET = indica que usaremos eL estandar de dirección IPv4 o el hostname
* SOCK_DGRAM = Corresponde a los sockets destinados a la comunicación en modo no conectado para el envío de datagramas de tamaño limitado.

Si ejecutamos el programa, nos regresara la data y detalles sobre el host remoto y el puerto.
"""