#1. Elabore um programa que solicita 2 números inteiros, e realize a divisão destes.

while True:
    print(" *Divisões Consecutivas*")
    valor1 =  input("digite o primeiro valor ou 'S' para sair:  ").upper()
    match valor1:
        case "S":
            print("PROGRAMA ENCERRADO!")
            break
    valor2 =  input("digite o segundo valor ou 'S' para sair:  ").upper()
    match valor2:
        case "S":
            print("PROGRAMA ENCERRADO!")
            break

    try:
        numero1 = int(valor1) 
        numero2 =  int(valor2)
        divisao = numero1 / numero2
        print(f" a divisão de {numero1} por {numero2} resulta em: {divisao} ")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        print("")
        print("Clique para continuar")
        input()


