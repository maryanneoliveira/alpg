'''
Elabore um algoritmo para que só possa autorizar a entrada na loja, àqueles que estão com a anuidade de associação em dia ou pagar o valor de 25 reais na entrada.
'''
print("para ter sua entrada autorizada, responda a seguinte questão: ")

anuidade_de_associação = input("você está em dia com a anuidade de associação? (sim ou não) ")

if (anuidade_de_associação == "sim"):
    print ("entrada autorizada!")
elif(anuidade_de_associação == "não"):
    print("você não tem permissão para entrar sem a anuidade com a associação a não ser que pague um valor de R$ 25,00")

    pagamento_entrada = input("você gostaria de pagar esse valor? (sim ou não) ")
    if (pagamento_entrada == "sim"):
        print("perfeito! então pode entrar!")
    
    else: 
        print("entrada não autorizada")