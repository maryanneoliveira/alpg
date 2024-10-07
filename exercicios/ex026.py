'''Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de uma feira, mas que só permite compras à vista.
'''

print("BEM VINDO(A) A FEIRA DA DONA MARY!")
cebola = 0.99
alho = 2.00
cenoura = 3.50
batata_inglesa = 3.75

print("CONFIRA NOSSOS PRODUTOS E SEUS VALORES POR UNIDADE:")
print(f"cenoura: {cenoura}\ncebola : {cebola}\nalho: {alho}\nbatata inglesa{batata_inglesa}")

cebola_quant = int(input("quantas cebolas você irá querer? "))
alho_quant = int(input("quantos alhos você irá querer? "))
cenoura_quant = int(input("quantas cenouras você irá querer? "))
batata_inglesa_quant = int(input("quantas batatas inglesas você irá querer? "))

total_a_pagar = ((cebola_quant*cebola) + (alho_quant*alho) + (cenoura_quant*cenoura) + (batata_inglesa_quant*batata_inglesa))

print(f" deu um total de R${total_a_pagar}")

forma_de_pagamento = input("Qual a forma de pagamento? ")

if(forma_de_pagamento == "a vista"):
    print("perfeito, me dê o valor e te darei seu troco!")
else:
    print("so aceitamos pagamentos a vista! essa opção não é valida!")