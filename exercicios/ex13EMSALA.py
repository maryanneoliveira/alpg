"""
Um salão de festa precisa verificar quem poderá entrar na festa, sabendo que para entrar, o responsável que está na porta de entrada precisa identificar 
solicitar o nome da pessoa e informar se encontrou na lista de convidados. 

Também, deverá informar se pessoa que deseja entrar é maior de idade. Se for menor,
 verificar se esta possui permissão de um responsável maior de idade autorizando a sua ida.

Para autorizar a entrada, a pessoa tem que estar na lista e deve ser maior de idade, 
ou poderá entrar se for menor mas com autorização e também deve constar na lista. 
Não atendendo a nenhuma dessas condições, a entrada não deve ser autorizada.
"""
#CONVIDADOS NA LISTA
convidado1 = "mary"
convidado2 = "igor"
convidado3 = "andre"
convidado = "andrezza"

nome_do_cliente = input("QUAL O SEU NOME? ").lower()

if(nome_do_cliente == convidado1 or nome_do_cliente ==convidado2 or nome_do_cliente == convidado3 or nome_do_cliente ==convidado):
    idade = int(input("Você esta na lista! Mas qual é a sua idade? "))
    if(idade >=18):
        print("VOCÊ PODE ENTRAR!")
    elif(idade<18):
        print("VOCÊ NÃO TEM IDADE!")
        autorizacao = input("MAS VOCÊ TEM AUTORIZAÇÃO? (sim/não)").lower()
        if (autorizacao == "sim"):
            print("VOCÊ PODE ENTRAR!")
        else:
            print("VOCÊ NÃO PODE ENTRAR!")
    

else:
    print("VOCÊ NÃO PODE ENTAR! SEU NOME NÃO ESTA NA LISTA!")
