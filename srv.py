import _thread
import socket
from datetime import datetime

HOST = '127.0.0.1'    # Endereco IP do Servidor
PORT = 5000           # Port do servidor

HOST_TV = '127.0.0.2'     # Endereco IP do Server TV
PORT_TV = 5001            # Porta do Server TV

timestamp = datetime.now()
count_normal = 1        # Contador para o número da senha normal
count_priority = 1      # Contador para o número da senha prioritária
count_N_chamadas = 0    # Contador de senhas normais chamadas(Requisitos da avaliação)
N_list = []             # Array contendo senhas normais a serem chamadas
P_list = []             # Array contendo senhas prioritárias a serem chamadas

# Criando função da conexão com o cliente
def ClientConnection(con, cliente, udp, dest):
    print (f'Conectado por', cliente, "\n")
    
    while True:
        # Especificando variáveis globais da função
        global count_normal,count_priority,count_N_chamadas
        global N_list,P_list
        
        msg = con.recv(1024).decode('utf-8') # Mensagem recebida do cliente
        
        if(msg == 'N'): # IF para chamada de senha normal
            msg = msg+str(count_normal)
            N_list.append(msg)
            print(timestamp, "- Senha",msg,"recebida\n")
            count_normal+=1
            
        elif(msg == 'P'): # IF para chamada de senha prioritária
            msg = msg+str(count_priority)
            P_list.append(msg)
            print(timestamp, "- Senha",msg,"recebida\n")
            count_priority+=1
            
        elif(msg == 'ENTER'): # IF para requisição de senha do TA
            if(count_N_chamadas < 2):
                if len(N_list) > 0:
                    msg_tcp = "senha "+str(N_list[0])   # Mensagem enviada para o TA
                    msg_udp = "Guichê 01 - senha "+str(N_list[0]) # Mensagem enviada para o TV
                    res_tcp = (msg_tcp).encode('utf-8')
                    res_udp = (msg_udp).encode('utf-8')
                    
                    con.send(res_tcp) # Enviando senha para o TA
                    print(timestamp, "- ",msg_tcp," enviado para o TA")
                    udp.sendto (res_udp, dest)  # Enviando mensagem para server TV
                    print(timestamp, "- ",msg_tcp," enviado para o TV\n")
                    
                    N_list.pop(0)
                    count_N_chamadas+=1
                    
                else:
                    res = ("\nNenhuma senha normal para chamar").encode('utf-8')
                    con.send(res)
            else:
                if len(P_list) > 0:
                    msg_tcp = "senha "+str(P_list[0])
                    msg_udp = "Guichê 01 - senha "+str(P_list[0])
                    res_tcp = (msg_tcp).encode('utf-8')
                    res_udp = (msg_udp).encode('utf-8')
                    
                    con.send(res_tcp)
                    print(timestamp, "- ",msg_tcp," enviado para o TA")
                    udp.sendto (res_udp, dest)  # Enviando mensagem para server TV
                    print(timestamp, "- ",msg_tcp," enviado para o TV\n")
                    P_list.pop(0)
                    count_N_chamadas=0
                    
                else:
                    res = ("\nNenhuma senha prioritária para chamar").encode('utf-8')
                    con.send(res)
                    
        if not msg: 
            print("\n Ocorreu um erro ao receber a mensagem!")
            break
        
        
    print ('\nFinalizando conexao do cliente', cliente)
    con.close()
    
# Configurando variáveis de conexão TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen()

#Configurando variáveis da conexão UDP (Server-TV)
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST_TV, PORT_TV)

print("Iniciando servidor principal!")
while True:
    # Utilizando função na criação da thread
    con, cliente = tcp.accept()
    _thread.start_new_thread(ClientConnection, (con, cliente, udp, dest))
   
   