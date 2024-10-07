'''Elabore um algoritmo que solicita duas informações do usuário. A primeira, pergunta se possui bolsa família (S ou N), e a segunda, se possui mais de três filhos (S ou N). Se for contemplado pelo bolsa família e possuir mais de três filhos, deverá retornar Verdadeiro, significando que pode acessar à vaga de cotista.'''

print("preencha as informações para descobrir se voce tem direito a cota: ")

bolsa_familia = int(input("voce tem acesso a bolsa familia? (1-sim e 2-não)" ))
qntd_filhos = int(input("voce tem mais de 3 filhos? (1-sim e 2-não) "))

if(bolsa_familia == 1 and qntd_filhos == 1):
    print("True")
    print("voce tem direito a cota!")
else:
    print("voce nao tem direito a cota!")