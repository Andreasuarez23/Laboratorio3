"""from socket import *

serverName = 'localhost'
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input("Escriba una frase en minúsculas:")
clientSocket.send(message.encode())

modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage.decode())

clientSocket.close()
"""

import re
from socket import *

serverName = 'localhost'
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Solicitar al usuario que escriba una frase
message = input("Escriba una frase en minúsculas: ")

# Verificar si el mensaje contiene solo caracteres alfabéticos
if re.match("^[a-zA-Z]*$", message):
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(2048)
    print(modifiedMessage.decode())
else:
    print("Error: El mensaje contiene caracteres no permitidos. Solo se permiten letras.")

clientSocket.close()