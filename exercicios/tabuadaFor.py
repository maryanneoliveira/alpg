#use o for para apresentar a tabuada de 1 até o 10

numeros_tabuada = [0,1,2,3,4,5,6,7,8,9,10];

for multiplicador  in range(1,11):
    for multiplicando in numeros_tabuada:
        print(f"{multiplicador} * {numeros_tabuada[multiplicando]} = {multiplicador * multiplicando:.0f} ")
    print()  

        
