import socket
HOST = '127.0.0.2'     # Endereco IP do Server TV
PORT = 5001            # Porta do Server TV


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

print("Monitor de senhas iniciado...\n")

while True:
    msg, cliente = udp.recvfrom(1024)
    msg = msg.decode('utf-8')
    
    print ("Última senha chamada: ", msg)