"""""
import re
from socket import *

serverName = 'localhost'
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Solicitar al usuario que escriba una frase
message = input("Escriba una frase en minúsculas: ")

# Verificar si el mensaje contiene solo caracteres alfabéticos
if re.match("^[a-z]*$", message):
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(2048)
    print(modifiedMessage.decode())
else:
    print("Error: El mensaje contiene caracteres no permitidos. Solo se permiten letras en minusculas.")

clientSocket.close()
"""

import re
from socket import *

# Configuración del servidor
serverName = 'localhost'
serverPort = 1200

# Crear el socket TCP para el cliente
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    # Intentar conectarse al servidor
    clientSocket.connect((serverName, serverPort))
    print(f"Conectado al servidor en {serverName}:{serverPort}")

    while True:
        # Solicitar al usuario que escriba una frase o "exit" para salir
        message = input("Escriba una frase en minúsculas (o 'exit' para salir): ")

        # Verificar si el usuario quiere terminar la conexión
        if message.lower() == 'exit':
            print("Terminando la conexión con el servidor.")
            break

        # Verificar si el mensaje contiene solo letras minúsculas y espacios
        if re.match("^[a-z ]*$", message):
            clientSocket.send(message.encode())
            modifiedMessage = clientSocket.recv(2048)
            print("Respuesta del servidor:", modifiedMessage.decode())
        else:
            print("Error: El mensaje contiene caracteres no permitidos. Solo se permiten letras en minúsculas y espacios.")
except Exception as e:
    print(f"Error en la conexión: {e}")
finally:
    # Cerrar el socket de forma segura
    clientSocket.close()
    print("Conexión cerrada.")