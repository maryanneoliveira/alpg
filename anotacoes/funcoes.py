#servem para reaproveitamento de codigo!
#OBS: FUNÇÕES DEVEM ESTAR NO INICIO DE CODIGO, POIS O PYTHON LÊ DE CIMA PARA A BAIXO (LINHA A LINHA)
saldo = 0

def exibir_saldo():
    print(f"Saldo = R${saldo}")

print("* Terminal bancário *")
print("1 - Saldo")
print("2 - Depositar")
print("3 - Sacar")
print("4 - Sair")

opcao = int(input("Escolha a opção: "))

match opcao:
    case 1:
        print("* Saldo na Conta *")
        exibir_saldo()
    case 2:
        print("* Depositar *")
        valor_deposito = float(input("Qual o valor a depositar? "))
        saldo += valor_deposito
        exibir_saldo()
    case 3:
        print("* Sacar *")
        valor_saque = float(input("Qual o valor a sacar? "))
        saldo -= valor_saque
        exibir_saldo()
    case _:
        print("Opção inválida")