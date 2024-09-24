"""
Q1. Verificação Básica de Igualdade: Peça ao estudante para escrever um programa que compara
 dois números (por exemplo, 10 e 20) usando o operador == e imprime o resultado.
"""

numero1 = int(input("digite o primeiro número: "));
numero2 = int(input("digite o segundo número: "));

if(numero1 == numero2):
    print( "esses numeros são iguais!")

else:
    print("esses números são diferentes!")

print("o numero 1 é:", numero1,"e o numero2 é:", numero2,"eles são iguais? verdareiro ou falso?")
print(numero1 == numero2)