'''Faça um algoritmo que lê dois números, e verifica se o primeiro número é maior ou igual ao segundo número. Se for, escrever "O número {valor do número 1} é maior ou igual ao número {valor do número 2}". Se não, escrever "O número {valor do número 1} é menor ou igual ao número {valor do número 2}".'''

numero1 = int(input("digite o 1º número: "));
numero2 = int(input("digite o 2º número: "));

if(numero1>= numero2):
    print(f"O número {numero1} é maior ou igual ao número {numero2}")
else:
    print(f"O número {numero1} é menor ou igual ao número {numero2}")