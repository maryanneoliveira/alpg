#lista 8, Q.1:
# Elabore um programa que realize a conversão de temperaturas de acordo com a opção escolhida pelo usuário. As opções de conversão estão listadas abaixo:

#Celsius para Kelvin
#Kelvin para Celsius
#Celsius para Fahrenheit
#Fahrenheit para Celsius

def celsius_para_kelvin():
    temperatura_celsius = float(input("Digite a temperatura em Celsius:(ex:30) "))
    temperatura_kelvin = temperatura_celsius + 273
    print("Temperatura em Kelvin: {:.2f}".format(temperatura_kelvin))
    input()

def kelvin_para_celsius():
    temperatura_kelvin = float(input("Digite a temperatura em Kelvin:(ex:40) "))
    temperatura_celsius = temperatura_kelvin - 273
    print("Temperatura em Celsius: {:.2f}".format(temperatura_celsius))
    input()

def celsius_para_fahrenheit():
    temperatura_celsius = float(input("Digite a temperatura em Celsius:(ex:50) "))
    temperatura_fahrenheit = temperatura_celsius * 1.8 + 32
    print("Temperatura em Fahrenheit: {:.2f}".format(temperatura_fahrenheit))
    input()

def fahrenheit_para_celsius():
    temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit:(ex:60) "))
    temperatura_celsius = (temperatura_fahrenheit - 32) / 1.8
    print("Temperatura em Celsius: {:.2f}".format(temperatura_celsius))
    input()


def menu( ):
   while True:
        print("1 - Celsius para Kelvin")
        print("2 - Kelvin para Celsius")
        print("3 - Celsius para Fahrenheit")
        print("4 - Fahrenheit para Celsius")
        print("5 - Encerrar o programa")
        entrada = int(input("Escolha a conversão que deseja:" ))
 
        match entrada:
           case 1: celsius_para_kelvin()
           case 2 : kelvin_para_celsius()
           case 3 : celsius_para_fahrenheit()
           case 4 : fahrenheit_para_celsius()
           case 5 : 
                print("Programa Encerrado!")
                break
           case _ : print("Opção invalida! Tente novamente ou digite 5 para sair")

#MAIN
menu()