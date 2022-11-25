import _thread
import socket

HOST = '127.0.0.1'    # Endereco IP do Servidor
PORT = 5000        # Port do terminal de senhas

count_normal = 1        # Contador para o número da senha normal
count_priority = 1      # Contador para o número da senha prioritária
count_N_chamadas = 0    # Contador de senhas normais chamadas(Requisitos da avaliação)
N_list = []             # Array contendo senhas normais a serem chamadas
P_list = []             # Array contendo senhas prioritárias a serem chamadas

# Criando função da conexão com o cliente
def ClientConnection(con, cliente):
    print (f'\nConectado por', cliente)
    
    while True:
        # Especificando variáveis globais da função
        global count_normal,count_priority,count_N_chamadas
        global N_list,P_list
        
        msg = con.recv(1024).decode('utf-8') # Mensagem recebida do cliente
        
        if(msg == 'N'): # IF para chamada de senha normal
            msg = msg+str(count_normal)
            N_list.append(msg)
            print ('\nSenha: ', msg, ' retirada!')
            count_normal+=1
            
        elif(msg == 'P'): # IF para chamada de senha prioritária
            msg = msg+str(count_priority)
            P_list.append(msg)
            print ('\nSenha: ', msg, ' retirada!')
            count_priority+=1
            
        elif(msg == 'ENTER'): # IF para requisição de senha do TA
            if(count_N_chamadas < 2):
                if len(N_list) > 0:
                    res_msg = "Guichê 01 - senha "+str(N_list[0])
                    res = (res_msg).encode('utf-8')
                    con.send(res)
                    N_list.pop(0)
                    count_N_chamadas+=1
                else:
                    res = ("Nenhuma senha normal para chamar").encode('utf-8')
                    con.send(res)
            else:
                if len(P_list) > 0:
                    res_msg = "Guichê 01 - senha "+str(P_list[0])
                    res = (res_msg).encode('utf-8')
                    con.send(res)
                    P_list.pop(0)
                    count_N_chamadas=0
                else:
                    res = ("Nenhuma senha prioritária para chamar").encode('utf-8')
                    con.send(res)
                    
        if not msg: break
        
        
    print ('\nFinalizando conexao do cliente', cliente)
    con.close()
    
# Configurando variáveis de conexão TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen()

print("Iniciando servidor principal!")
while True:
    # Utilizando função na criação da thread
    con, cliente = tcp.accept()
    _thread.start_new_thread(ClientConnection, (con, cliente))
   
   