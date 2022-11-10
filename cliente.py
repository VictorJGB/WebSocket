import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+C\n')
msg = input("Qual senha você deseja retirar: N - Normal  P - Prioritária: ").encode('utf-8')
while msg != '\x18':
    tcp.send (msg)
    msg = input("Deseja retirar outra senha? N - Normal  P - Prioritária: ").encode('utf-8')
tcp.close()