import _thread
import socket

HOST = '127.0.0.1'    # Endereco IP do Servidor
TS_PORT = 5000        # Port do terminal de senhas
TA_PORT = 5001        # Porta do terminal de atendimento

count_normal = 1        # Contador para o número da senha normal
count_priority = 1      # Contador para o número da senha prioritária
count_N_chamadas = 0    # Contador de senhas normais chamadas(Requisitos da avaliação)
N_list = []             # Array contendo senhas normais a serem chamadas
P_list = []             # Array contendo senhas prioritárias a serem chamadas

def ClientConnection(con, cliente):
    print (f'Conectado por', cliente)
    
    while True:
        msg = con.recv(1024).decode('utf-8') # Mensagem recebida do cliente
        if(msg == 'N'): # If para chamada de senha normal
            msg = msg+str(count_normal)
            N_list.append(msg)
            count_normal=+1
            print ('Senha: ', msg, ' retirada!')
            
        elif(msg == 'P'): # If para chamada de senha normal
            msg = msg+str(count_priority)
            P_list.append(msg)
            count_priority=+1
            print ('Senha: ', msg, ' retirada!')
            
        elif(msg == null or msg == ''): # If para requisição de senha do TA
            if(count_N_chamadas < 2): # Verificação de requisito da avaliação
                res = 'N'+str(count_normal).encode('utf-8')
                con.send(res)
            else:
                res = 'P'+str(count_priority).encode('utf-8')
                con.send(res)
                    
        if not msg: break
        
        
    print ('Finalizando conexao do cliente', cliente)
    con.close()
    

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, TS_PORT)
tcp.bind(orig)
tcp.listen()

while True:
    con, cliente = tcp.accept()
    _thread.start_new_thread(ClientConnection, (con, cliente))
   
   