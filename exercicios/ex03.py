'''Q4. Escreva um algoritmo que leia o nome de uma pessoa, o ano em que ela nasceu. Em seguida imprima uma mensagem que diga "Olá, [nome], hoje você tem [idade] anos". Considere que os dados de entrada devem ser armazenados em variáveis distintas, e o cálculo da idade deve se basear no ano atual.
'''

nome = input("Qual o seu nome? ");
ano_de_nascimento = int(input("qual o ano de seu nascimento? "));
idade = 2024- ano_de_nascimento
print("Olá", nome,"hoje você tem",idade,"anos" );