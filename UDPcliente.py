from socket import *

serverName = 'localhost'
serverPort = 12000
try:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(5)
    
    # Leer un único mensaje del usuario
    message = input('Escriba una frase en minúsculas: ')

    if not message:
        print("Error: El mensaje no puede estar vacío")
    
    else:
        letras = True
        for i in message:
            if not ("a" <= i <= "z" or "A" <= i <= "Z"):
                letras = False
        
        if not letras:
            print("Error: El mensaje solo puede contener letras")
        else:
            # Enviar el mensaje al servidor
            clientSocket.sendto(message.encode(), (serverName, serverPort))

            # Recepción del mensaje modificado del servidor
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

            # Mostrar el mensaje modificado
            print('Respuesta del servidor:', modifiedMessage.decode())

except timeout:
    print("Error: Tiempo de espera agotado. El servidor no responde.")
except ValueError as ve:
    print(f"Error de valor: {ve}")
except Exception as e:
    print(f"Se produjo un error: {e}")
finally:
    clientSocket.close()