"""anotações da aula do dia 09/09/2024"""

#Pascal Case combina palavras colocando todas com a primeira letra maiúscula

NomeDoAluno = "maryane"
Idade = 18

#Em snake case, utilizamos underline no lugar do espaço para separar as palavras.

meu_nome = "maryane"
minha_idade = 18

#Camel case deve começar com a primeira letra minúscula e a primeira letra de cada nova palavra subsequente maiúscula:

nomeMeu = "maryane"
idade_Minha = 18

"""
lembrando também das regras de não usar palavras reservadas (if, else,for,algorítimo e etc), palavras com acentos, caracteres especiais, espaços e etc para nomear um atributo.
"""

#ANALISTA DE REQUISITOS VAI VERIFICAR TUDO QUE O PROJETO PRECISA, ELE ANALISA.

'''OPERADORES LÓGICOS
True ou False (do tipo booleano), usamos para fazer comparações.
'''

print("ola" == "Ola") #verifica se são iguais
#retorna False, pois não é igual. por conta das letras maiúscula e minuscula

print("ola" != "Ola") #verifica se são diferentes
#retorna verdadeiro, pois são diferentes. python é case sensitivy, ela diferencia letras maiúsculas ou minúsculas

print(20 == "20)") #false
print ( 20 > 39) #false
print(1 <= 19) #true