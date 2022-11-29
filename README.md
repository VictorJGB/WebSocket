# websockets_project
<h2>Trabalho para nota N2 na disciplina de Sistemas Distribuídos do curso Sistemas de Informação</h1>
<br>
Esse projeto consiste em implementar os conhecimentos sobre web socket estudados na disciplina através de conexões client-cerver (TCP e UDP).
<br> <br>
<strong>Em resumo temos o 4 serviços rodando ao mesmo tempo: </strong>
<h3> Servidor principal </h2>
<br> Encarregado de receber,gerenciar e encaminhar as senhas para os outros serviços. <br>
<h3> Terminal de senhas </h3>
<br> Encarregado de enviar as senhas retiradas <br>
<h3> Terminal de Atendimento </h3>
<br> Encarregado de requisitar do server principal uma senha para atender <br>
<strong> OBS:A cada 2 senhas normais 1 prioritária deve ser chamada </strong>
<br>
<h3> Monitor de senhas </h3>
<br> Encarregado de mostrar "na tela" a última senha chamada para atendimento </br>
