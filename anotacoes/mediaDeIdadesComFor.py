#calculando a media de idades de 10 alunos com for:
media_idades = 0
for i in range(10):
    idade = int(input("DIGITE SUA IDADE:"))
    media_idades = media_idades + idade

print(f"a media das idades é: {media_idades/10}")