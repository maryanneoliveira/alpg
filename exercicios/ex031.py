#lista 8, Q.2:

''' Elabore um programa que simula um terminal bancário. Ao iniciar o programa, deve apresentar ao usuário um menu de opções, como a seguir:
Ver saldo
Depositar
Sacar
Extrato
Sair

1. O programa só deverá ser encerrado se o usuário escolher a opção 5. Caso escolha uma opção diferente de 1 a 5, informar que é uma opção inválida.

2. A opção 1 deve apresentar o saldo da conta.
A opção 2 deve solicitar o valor a ser depositado.
Será considerado válido, somente se o valor para depósito for maior que 0.
Se digitar um valor válido, realizar a operação de depósito. Esta operação deverá ser registrada para que possa ser exibida no extrato.
Se digitar um valor inválido, não realizar a operação, informar que o valor é inválido ao usuário, e solicitar o valor novamente.

3. A opção 3 deve solicitar o valor a ser sacado.
Será considerado válido, somente se o valor do saque for maior que 0 e nunca maior que o valor do saldo.
Se digitar um valor válido, realizar a operação de saque. Esta operação deverá ser registrada para que possa ser exibida no extrato.
Se digitar um valor inválido, não realizar a operação, informar que o valor é inválido ao usuário, e solicitar o valor novamente.

4. A opção 4 deve apresentar toda a movimentação ocorrida na conta. 
Para apresentar uma operação que foi realizada de saque, deve aparecer um valor negativo antes do valor.
Para apresentar uma operação de depósito, apenas apresentar o  número sem sinal na frente. 
Ao final de todas as operações realizadas, mostrar o saldo da conta.

A opção 5 deve apresentar a mensagem "Programa encerrado", e encerrar o programa.

'''
saldo = 0
movimentacoes = []

def exibir_saldo():
    print(f"Saldo = R${saldo}")
    input()

def validarValorOperacoes(valorOperacao):
    if valorOperacao <= 0:
        return False;
    return True;
    
def depositar():
    global saldo;
    print("* Depositar *")
    valor_deposito = float(input("Qual o valor a depositar? "))
    
    if validarValorOperacoes(valor_deposito):
        saldo += valor_deposito
        movimentacoes.append(valor_deposito)
        exibir_saldo()
    else:
        print("Erro: Valor inválido para depósito!");
        depositar()
    
    
def sacar():
    global saldo
    print("* Sacar *")
    valor_saque = float(input("Qual o valor a sacar? "))
    
    if validarValorOperacoes(valor_saque) and valor_saque <= saldo:
        saldo -= valor_saque
        movimentacoes.append(valor_saque * -1)
        exibir_saldo()
    else:
        print("Erro: Valor inválido para saque ou valor insuficiente");
        sacar()
    

def extrato():
    print("* Extrato *")
    print("")
    if len(movimentacoes) > 0 :
     for i in movimentacoes:
        print(i)
    else:
        print("nenhuma movimentação realizada")
    exibir_saldo()
    
def menu():
    while True:
        print("* Terminal bancário *")
        print("1 - Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4- Extrato")
        print("5 - Sair")

        opcao = int(input("Escolha a opção: "))

        match opcao:
            case 1:
                print("* Saldo na Conta *")
                exibir_saldo()
                
            case 2:
                depositar()
            case 3:
                sacar()
            case 4:
                extrato() 
            case 5:
                print("Programa Encerrado!")
                break
            case _:
                print("Opção inválida")
                input()
                
menu()