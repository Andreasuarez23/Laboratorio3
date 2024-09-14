from socket import *

# Configuración del servidor
serverPort = 1200
serverSocket = socket(AF_INET, SOCK_STREAM)

# Enlazar el socket a la dirección IP y puerto
serverSocket.bind(('localhost', serverPort))

# Poner el socket en modo de escucha
serverSocket.listen(1)
print(f"El servidor está listo para recibir conexiones en el puerto {serverPort}...")

while True:
    try:
        # Aceptar la conexión de un cliente
        connectionSocket, addr = serverSocket.accept()
        print(f"Conexión establecida con {addr}")

        while True:
            # Recibir datos del cliente
            message = connectionSocket.recv(2048).decode()

            if not message:
                break

            # Convertir el mensaje a mayúsculas como respuesta
            modifiedMessage = message.upper()

            # Enviar el mensaje modificado de vuelta al cliente
            connectionSocket.send(modifiedMessage.encode())

        connectionSocket.close()
        print(f"Conexión con {addr} cerrada.")
    except Exception as e:
        print(f"Error en el servidor: {e}")
        break

# Cerrar el socket del servidor cuando se termina
serverSocket.close()
