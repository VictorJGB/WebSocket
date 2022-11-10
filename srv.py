import socket
HOST = '127.0.0.1'    # Endereco IP do Servidor
TS_PORT = 5000        # Port do terminal de senhas
TA_PORT = 5001        # Porta do terminal de atendimento
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, TS_PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print (f'Conectado por', cliente)
    while True:
        msg = con.recv(1024).decode('utf-8') # Mensagem recebida do cliente
        if not msg: break
        print ('Senha: ', msg)
    print ('Finalizando conexao do cliente', cliente)
    con.close()