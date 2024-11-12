#REFATORANDO O CODIGO INICIAL! 
saldo = 0

#EXIBIR SALDO 
def exibir_saldo():
    print(" Carregando Saldo....")
    print(f"Saldo = R$ {saldo}")
    input()

#DEPOSITAR
def depositar():
     global saldo
     print("* Deposito *")
     valor_deposito = float(input("Qual o valor que deseja depositar? "))
     saldo += valor_deposito
     exibir_saldo()
     
#SACAR
def sacar():
     global saldo
     print("* Saque *")
     valor_saque = float(input("Qual o valor a sacar? "))
     saldo -= valor_saque
     exibir_saldo()

#MENU

def menu():
    while True: #vai rodar o menu ate ser falso ou eu pedir para parar (BREAKE)
        print("* Terminal bancário *")
        print("1 - Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")
        opcao = int(input("Escolha a opção desejada: "))

        match opcao:
            case 1:
                exibir_saldo()
            
            case 2:
                depositar()
                        
            case 3:
                sacar()
                    
            case 4:
                print("fim")
                break
            case _:
                print("Opção inválida")
                input()
                    
                        


menu()



