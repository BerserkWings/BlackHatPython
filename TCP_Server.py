"""Vamos a crear un servidor TCP que estara de manera local, osea que la IP seria 127.0.0.1"""

import socket, threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Escuchando en {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Aceptando Conexion de {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recibido: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()

"""
Si utilizamos el programa que hicimos del TCP_Client y tan solo cambiamos la IP por la local, mientras esta activo el 
servidor, obtendremos una respuesta ACK, ya que se esta haciendo un Three-Way Handshake. Y en el servidor, se vera la 
conexion que hubo con un puerto aleatorio y el host que pusimos en el programa TCP_Client.
"""