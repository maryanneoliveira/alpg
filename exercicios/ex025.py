'''Faça um algoritmo que irá fazer o cadastro de usuário. Para isso, solicita o nome do usuário, 
e a senha. Depois, pede que o usuário confirme novamente a senha.
 O sistema deverá verificar se as senhas digitadas são iguais. Se forem iguais, informar que o cadastro está correto.
 Se não forem iguais, informar que o cadastro não foi realizado porque as senhas não conferem.'''
 
print("VAMOS INICIAR SEU CADASTRO...")
nome = input("Digite seu nome:(ex: João,Paulo,Maria...) ")
senha = int(input("Digite sua senha númerica com 4 digitos: "))
senha_confirmar = int(input("confirme sua senha: "))

if(senha == senha_confirmar):
    print("senhas iguais! seu cadastro está completo")
else:
    print("cadastro não realizado, pois suas senhas são diferentes! tente novamente.")