# Elabore um programa de conversão de temperatura. Para isso, terá duas opções de conversão.
#Deverá então apresentar um menu que apresenta 3 opções:
    #1. Celsius para Farenheit
    #2. Celsius para Kelvin
    #3. Sair

    #O programa só será encerrado se for escolhida a opção 3. Ou seja, após realizar uma operação, deverá retornar ao menu.
def celsius_para_farenheit():
    temperatura_celsius = float(input("Digite a temperatura em Celsius:(ex:50) "))
    temperatura_fahrenheit = temperatura_celsius * 1.8 + 32
    print("Temperatura em Fahrenheit: {:.2f}".format(temperatura_fahrenheit))
    input()

def celsius_para_kelvin():
    temperatura_celsius = float(input("Digite a temperatura em Celsius:(ex:30) "))
    temperatura_kelvin = temperatura_celsius + 273.15
    print("Temperatura em Kelvin: {:.2f}".format(temperatura_kelvin))
    input()

def menu():
    while True:
        print(" * SISTEMA DE CONVERSÕES * ")
        print("1 - Celsius para Farenheit")
        print("2 - Celsius para Kelvin")
        print("3 - Sair")

        entrada = int(input("Escolha a opção desejada: "))

        match entrada:
            case 1:
                print(" Celsius ---> Farenheit")
                celsius_para_farenheit()

            case 2 : 
                print(" Celsius ---> Kelvin")
                celsius_para_kelvin()
            case 3 : 
                print("Programa encerrado!")
                break

menu()