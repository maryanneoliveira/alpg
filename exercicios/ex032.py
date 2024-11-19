#lista 8, Q.3:
'''
Q3. Elabore um jogo de adivinhação de número de 1 a 100 mais robusto, de modo que possua o seguinte menu (função específica):
Sete chutes
Cinco chutes
Três chutes
Sair

O usuário deverá escolher uma opção de 1 a 4.

Se escolher 1, o programa deverá permitir que dê no máximo 7 chutes. Se escolher 2, serão 5 chutes, e se for 3, terá 3 chutes.

Se escolher a opção 4, deverá encerrar o programa.

Funções mínimas que deverão ter no programa.
Solicitar chute (sem parâmetro):
O programa deverá solicitar um chute do usuário.
O programa deverá validar o chute dado, chamando uma função específica.
Validar chute (recebe como parâmetro o chute dado):
Se o chute foi fora do intervalo de 1 a 100, informar "Chute dado está fora do intervalo de 1 a 100", e não subtrair da quantidade de chances.
Se o chute já foi dado antes, informar, e não subtrair da quantidade de chances.
Se o chute for igual, informar "Você acertou!", informar com quantos chutes dados acertou o número, e encerrar o programa.
Se o chute for menor, informar que "Você errou! Chute foi menor que o número secreto!".
Se o chute for maior, informar que "Você errou! Chute foi maior que o número secreto!".
Menu
Deverá apresentar a tela com as opções para o jogo.
'''
chances = 1
def menu():
    while True:
        print(" ")
        print(" Jogo de Adivinhação ")
        print("1 - Sete Chutes")
        print("2 - Cinco Chutes")
        print("3 - Três Chutes")
        print("4 - Sair")
        print("=====================")

        opcao = int(input("Escolha uma opção: "))
        global chances

        match opcao:
            case 1: chances = 7
            case 2: chances = 5
            case 3: chances = 3
            case 4: 
                print("Fim de Jogo!")
                break
            case _:
                print("opção invalida!")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
menu()