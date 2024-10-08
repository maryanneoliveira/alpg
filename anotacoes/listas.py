#o indice de uma lista sempre inicia na posição 0

lista = [] #lista vazia

idades = [10,20,30] #lista com 3 itens, de indices 0,1 e 2 respectivamente

print(idades[2]) #me mostre o valor de indice 2 da lista "idades"

print(idades) #mostre a lista completa 

#MOSTRANDO A LISTA ELEMENTO POR ELEMENTO USANDO FOR
soma_idades = 0

for i in idades: #para i no intervalo de idades, i assume cada um dos elementos, começando de 0 e terminando no ultimo
    print(i)
    soma_idades += i #soma idades recebe ela mesma e i acada loop

print(f"a media das idades é de: {soma_idades/len(idades)} ") #LEN É UMA FUNÇÃO QUE NOS AJUDA A DESCOBRIR O TAMANHO DA LISTA QUANDO NÃO SABEMOS

#ADICIONANDO ITENS NA LISTA

nomes = []

nomes.append("mary") #adiciona ao fim
nomes.append("jardiel")
nomes.append('val')

print(nomes)