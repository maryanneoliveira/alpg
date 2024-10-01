
"""numero = 5
for i in range (numero): #RANGE = INTERVALO, para i no intervalo de tamanho = numero
    print (i)  #i é cada um desse intervalo (numero -1, pois ele começa em zero)

    """

#faça um jogo de adivinhação para descobrir o numero secreto

numero_secreto = 12;
chance = 0;

print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
print("1 - 5 chances")
print("2 - 3 chances")
print("3 - 1 chances")


nivel = int(input("escolha o nível (1-3) desejado:"))

if (nivel == 1):
    chance = 5;
elif (nivel == 2):
    chance = 3;
elif (nivel == 3):
    chance = 1;
else:
    print("o valor digitado é incorreto! rode novamente ")

for i in range (chance):
   tentativa = int(input( "digite sua tentativa: "))
   if (tentativa == numero_secreto):
       print("VOCÊ ACERTOU!")
       break
   else :
       print("VOCÊ ERROU")

print("FIM DE JOGO")