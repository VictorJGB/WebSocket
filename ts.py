import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print("Iniciando conexão com servidor... \n")

while True:
    msg = input("\n ----- Retire uma senha ----- \n N - Normal  P - Prioritária: ")
    
    if(msg == "N" or msg == "P"):
        msg_encode = msg.encode('utf-8')
        tcp.send (msg_encode)
        print("Senha retirada!")
    else:
        print("\n Erro ao retirar senha!")