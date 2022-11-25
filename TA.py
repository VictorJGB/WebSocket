import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta do servidor

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print("Iniciando conexão com servidor... \n")

while True:
    if not input("\n Digite ENTER para chamar uma nova senha..."):
        msg = str("ENTER").encode('utf-8')
        tcp.send (msg)
        response = tcp.recv(1024).decode('utf-8') #Resposta do servidor
        print(response)
    else: print("\n Erro ao enviar a mensagem!")