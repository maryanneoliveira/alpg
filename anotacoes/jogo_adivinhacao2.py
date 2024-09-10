#ELIF,
#MOSTRA SE ACERTOU, E SE ERROU SE O CHUTE FOI MAIOR OU MENOR

numero_secreto = 8;

chute =  int(input("digite seu chute: "));

if(chute == numero_secreto): #se os numeros forem iguais
    print("Você acertou") #mostre VOCE ACERTOU

elif (chute > numero_secreto): #se não, se 
    print("o chute foi maior")
else:
    print("chute menor")

#O ELSE NÃO TEM CONDIÇÃO ENTRE PARENTESES