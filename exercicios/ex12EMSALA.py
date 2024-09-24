"""
Um salão de festa precisa verificar quem poderá entrar na festa, sabendo que para entrar, o responsável que está na porta de entrada precisa identificar 
solicitar o nome da pessoa e informar se encontrou na lista de convidados. 

Também, deverá informar se pessoa que deseja entrar é maior de idade. Se for menor,
 verificar se esta possui permissão de um responsável maior de idade autorizando a sua ida.

Para autorizar a entrada, a pessoa tem que estar na lista e deve ser maior de idade, 
ou poderá entrar se for menor mas com autorização e também deve constar na lista. 
Não atendendo a nenhuma dessas condições, a entrada não deve ser autorizada.
"""

nome_da_pessoa = input("QUAL O SEU NOME? ").lower()
idade = int(input("QUAL A SUA IDADE? "))

if((nome_da_pessoa == "mary" or nome_da_pessoa == "andre" or nome_da_pessoa == nome_da_pessoa == "igor" or nome_da_pessoa == "andrezza") and idade>=18):
    print("PODE ENTRAR!")

elif((nome_da_pessoa == "mary" or nome_da_pessoa == "andre" or nome_da_pessoa == nome_da_pessoa == "igor" or nome_da_pessoa == "andrezza") and idade<18):
    autorizacao = input("VOCÊ TEM AUTORIZAÇÃO? (sim/não)").lower()
    if(autorizacao =="sim"):
        print("PODE ENTRAR!")
    else:
        print("NÃO PODE ENTRAR!")

else:
        print("NÃO PODE ENTRAR!")

#resposta incorreta, pois apesar de funcionar não esta didático