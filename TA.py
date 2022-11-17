import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print("Iniciando conexão com servidor... \n")

while True:
    msg = input("Digite ENTER para chamar uma nova senha").encode('utf-8')
    tcp.send (msg)
    
tcp.close()