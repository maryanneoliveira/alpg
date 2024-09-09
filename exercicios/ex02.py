"""
 Faça um programa que leia o nome de uma pessoa e a sua idade. Imprima uma mensagem que diga "Olá, [nome]. Você terá  [idade] anos daqui a 10 anos". Os dados de entrada devem ser armazenados em variáveis distintas.

"""

nome = input("qual é o seu nome? ");
idade_atual = int(input("qual a sua idade? "));
idade_futura = idade_atual+10
print("Olá", nome,"você terá", idade_futura,"anos daqui 10 anos." )