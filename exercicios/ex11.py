"""
receba 3 dados: n1,n2 e se tem bom comportamento, depois calcula a média e ve se esta aprovado, se a media>=6: aprovado
se media<6 solicita a nota da recuperação

se nota_rec>=6 : passou
se nota_rec >=5 and <6 :
 ve se tem bom comportamento
   se tiver bom comportamento: passou 
   senão reprovou
senão: reprovou

"""

nota1 = float(input("DIGITE A PRIMEIRA NOTA: "));
nota2 = float(input("DIGITE A SEGUNDA NOTA: "));


media = ((nota1+nota2)/2)
print(" a média do aluno é:", media)

if(media >= 6): 
    print("VOCÊ ESTÁ APROVADO!")

elif(media>=5): 
    nota_rec = float(input("DIGITE A NOTA DE SUA RECUPERAÇÃO: "))
    comportamento = input("QUAL O COMPORTAMENTO DO ALUNO?(BOM/RUIM)").upper() #upper coloca todas as letras maiusculas

    if(nota_rec>=6):
        print("VOCÊ ESTÁ APROVADO POR NOTA DA RECUPERAÇÃO!")

    elif(nota_rec>=5 and comportamento == "BOM"):
        print("VOCÊ ESTÁ APROVADO POR BOM COMPORTAMENTO!")

    else:
        print("REPROVADO NA RECUPERAÇÃO!")

else:
    print("REPROVADO!")

