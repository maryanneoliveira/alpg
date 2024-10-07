print("BEM-VINDO(A) À FEIRA DA DONA MARY!")
em_dia = input("Você está em dia com a sociedade agrícola? (sim ou não): ").lower()

if (em_dia == "sim"):
    cebola = 0.99
    alho = 2.00
    cenoura = 3.50
    batata_inglesa = 3.75

    print("\nCONFIRA NOSSOS PRODUTOS E SEUS VALORES POR UNIDADE:")
    print(f"Cenoura: R${cenoura:.2f}\nCebola: R${cebola:.2f}\nAlho: R${alho:.2f}\nBatata Inglesa: R${batata_inglesa:.2f}")

   
    cebola_quant = int(input("\nQuantas cebolas você irá querer? "))
    alho_quant = int(input("Quantos alhos você irá querer? "))
    cenoura_quant = int(input("Quantas cenouras você irá querer? "))
    batata_inglesa_quant = int(input("Quantas batatas inglesas você irá querer? "))

    total_a_pagar = (cebola_quant * cebola) + (alho_quant * alho) + (cenoura_quant * cenoura) + (batata_inglesa_quant * batata_inglesa)
    print(f"\nTotal a pagar: R${total_a_pagar:.2f}")

  
    forma_de_pagamento = input("Qual a forma de pagamento? ").lower()

    if forma_de_pagamento == "a vista":
        dinheiro = float(input("Qual o valor que você tem para pagar? R$"))

        if dinheiro >= total_a_pagar:
            troco = dinheiro - total_a_pagar
            print(f"Compra realizada com sucesso! Seu troco é de R${troco:.2f}.")
        else:
            print("Você não tem dinheiro suficiente para pagar essa compra.")
    else:
        print("Só aceitamos pagamento à vista. Sinto muito!")
else:
    print("Infelizmente, só vendemos para pessoas que estão em dia com a sociedade agrícola! Sinto muito.")
