from socket import *

serverPort = 12000

try:
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    print("El servidor está listo para recibir")

    while True:
        try:
            message, clientAddress = serverSocket.recvfrom(2048)

            if not message:
                raise ValueError("Mensaje recibido está vacío")
            modifiedMessage = message.upper()
            serverSocket.sendto(modifiedMessage, clientAddress)

        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except Exception as e:
            print(f"Se produjo un error al procesar el mensaje: {e}")

except Exception as e:
    print(f"Se produjo un error en el servidor: {e}")
finally:
    serverSocket.close()
