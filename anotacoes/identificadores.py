# são as constantes, variaveis e etc, e serve para guardar um valor/ uma informação, e elas ficam guardadas na memória do meu programa.

'''
ano_nascimento = 2005;
print("Nasceu em",ano_nascimento);

ano_atual = 2024;
print("Tem", (ano_atual-ano_nascimento),"anos");
'''

#no python, não existe uma variável constante, a qual eu não possa modificar o valor. então uma constante, é uma variável que eu não mexo no valor. 
#OBS: normalmente para indicar uma constante, eu escrevo o nome da variável tudo maiusculo (ex: NOME = mary)


#ENTRADA DE DADOS 
'''
ano_nascimento = input("qual seu ano de nascimento? ");
print(type(ano_nascimento)); #vai dizer que é string, pois tudo que vem do input, vem como texto, é preciso então converter para inteiro

'''



ano_nascimento = int(input("qual seu ano de nascimento? "));
ANO_ATUAL = 2024;

print("Nasceu em",ano_nascimento);
print("Tem", (ANO_ATUAL-ano_nascimento),"anos");
