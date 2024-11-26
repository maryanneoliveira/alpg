# a apartir do momento que temos uma string, podemos fazer algumas coisas com ela...

nome = "maryane santos de oliveira"

#VER O TAMANHO
print(len(nome))  #LEN mostra o tamanho COM OS ESPAÇOS!!

#COLOCAR TUDO EM MAIUSCULO
print(nome.upper())

#COLOCAR TUDO EM MINUSCULO
estado_civil= "SOLTEIRA"
print(estado_civil.lower())

#VER SE É NUMERICO
if "18".isalpha():  #ve se em so letras
    print("é alpha, apenas letras")

if "18".isnumeric():  #ve se em so numeros
    print("é numerico, apenas mumeros")

if "18 anos".isalnum:   #ve se tem letras e numeros 
    print("é alfanumerico, tem letras e numeros")

print(nome.isalnum())

#isdigit() e isnumeric() :
# isdigit verificxa apenas se é um numero inteiro e positivo, e não considera numeros negativos e decimais
# isnumeric() abrange tudo, negativos,positivos e decimais

#REMOVER ESPAÇOS 
   #DO INICIO E DO FINAL:
frase1 = "      esta frase tem espaços no inicio e no final       "
print(frase1.strip())
#obs: temos o leftstrip() e o rihgtstrip() que remove apenas os espaços do inicio e do final da frase respectivamente

    #NO MEIO:
frase2 = " e        sta frase tem espaços no inicio e no fina       l"
print(frase1.replace(" ", ""))

#VER SE COMEÇA COM ALGO

print(nome.upper().startswith("MAR")) #ve se o nome (ja em maiusculo começa com 'mar')
  #obs tem tambem o endwith pra ver se termina com algo

#ENCONTRAR NA FRASE
print(nome.find("y")) #mostra em que posição esta tal coisa 

#CONTAR QUANTOS TEM
nome2 = "maryane santos maryane"
print(nome2.count("mary"))

