#ESTRUTURAS DE REPETIÇÃO

"""imagina se quisessemos pedir 10 idades de 10 alunos..."""

#o codigo ficaria:
""""   
idade1 = int(input("digite sua idade"))
idade2 = int(input("digite sua idade"))
idade3 = int(input("digite sua idade"))
idade4 = int(input("digite sua idade"))
idade5 = int(input("digite sua idade"))
idade6 = int(input("digite sua idade"))
idade7 = int(input("digite sua idade"))
idade8 = int(input("digite sua idade"))
idade9 = int(input("digite sua idade"))
idade10 = int(input("digite sua idade"))

 """

#apesar de funcionar está muito repetitivo, para isso, temos as estruturas de repetição!!

#FOR : DE ---> PARA

"""

for i in range(10):   #para i no intervalo de: 10
    idade = int(input("Digite sua idade: ")) #repita isso

    """
#NO CASO ACIMA APENAS A LINHA 25 PERTENCE AO FOR, O RESTO SÃO AS DIRETRIZES DESSE FOR

#ADICIONANDO INTERALOS ESPECIFICOS:

#INICIO E FIM

for i in range (50,100): #começa em 50 e vai atev100-1 (porem repete 50x)
    print(i)

print("")

#INICIO , FIM E COMPORTAMENTO

for i in range (50,100,2): #começa em 50 e vai ate100-1 ( PULANDO DE 2 EM 2
    print(i)

print("")
#DECRESCENDO

for i in range (100,49,-1): #começa em 100 e vai ate 49-(-1) = 50  DIMINUINDO 1 EM 1
    print(i)

print("")




