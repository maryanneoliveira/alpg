#Faça um programa que solicita 5 números inteiros. Ao final, informe o menor e o maior número digitado.

numero1 = int(input("digite o 1° numero: "))
numero2 = int(input("digite o 2° numero: "))
numero3 = int(input("digite o 3° numero: "))
numero4 = int(input("digite o 4° numero: "))
numero5 = int(input("digite o 5° numero: "))

maior_numero = 0

if(numero1 > numero2 and numero1 > numero3 and numero1 > numero4 and numero1 > numero5) :
    maior_numero = numero1

elif( numero2 > numero3 and numero2 > numero4 and numero2 > numero5) :
   maior_numero = numero2

elif (numero3 > numero4 and numero3 > numero5) :
    maior_numero = numero3

elif( numero4 > numero5) :
    maior_numero = numero4

else:
    maior_numero = numero5


print(f"o maior numero é: {maior_numero}")

menor_numero = 0

if(numero1 < numero2 and numero1 < numero3 and numero1 < numero4 and numero1 < numero5) :
    menor_numero = numero1

elif( numero2 < numero3 and numero2 < numero4 and numero2 < numero5) :
   menor_numero = numero2

elif (numero3 < numero4 and numero3 < numero5) :
    menor_numero = numero3

elif( numero4 < numero5) :
    menor_numero = numero4

else:
    menor_numero = numero5


print(f"o menor numero é: {menor_numero}")


"""percebe-se que ao descer nas comparações as condições foram diminuindo,
 isso acontece porque se o primeiro if não deu certo quer dizer 
 que aquele número já não é o maior/menor, entçao não precisa repetir"""

