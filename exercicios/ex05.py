"""Q6. Escreva um algoritmo que solicita ao usuário uma quantidade de tempo em segundos e então a converte para horas. Por exemplo, se o usuário inserir 3666 segundos, o programa deve imprimir "1 hora", sem considerar os segundos restantes.
"""

segundos = int(input("digite a quantidade de tempo em segundos: "))
horas = round(segundos/3600); #ROUND arredonda sem se importar com as casas após a virgula

print("esse tempo em horas equivale a",horas,"hora(s).")