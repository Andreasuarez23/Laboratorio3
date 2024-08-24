from socket import *

serverName = 'localhost'
serverPort = 12000

try:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(5)

    message = input('Escriba una frase en minúsculas: ')

    if not message:
        raise ValueError("El mensaje no puede estar vacío")

    clientSocket.sendto(message.encode(), (serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print('Respuesta del servidor:', modifiedMessage.decode())

except timeout:
    print("Error: Tiempo de espera agotado. El servidor no responde.")
except ValueError as ve:
    print(f"Error de valor: {ve}")
except Exception as e:
    print(f"Se produjo un error: {e}")
finally:
    clientSocket.close()
