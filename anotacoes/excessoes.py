#servem para garantir que o programa vai continuar, mesmo com algum erro.
'''
def m2():
    print("inicio m2")
    numeros = [0,5,4]
    print(numeros[3]) #dará erro, pois a lista tem ate o indice 2 (0,1 e 2)
    print("fim m2")

def m1():
    print("inicio m1")
    m2();
    print("fim m2")

def main():
    print("inicio main")
    m1();
    print("fim main")


main()

'''

"""
o código acima irá falhar apos mostrar na tela "INICIO M2" 
pois tera um erro. aplicamos então excessões para tentar 
seguir em fente mesmo com os erros.
"""

#try = tente executar isso
#except = se não conseguir, faça algo

#CODIGO MELHORADO:
'''
def m2():
    print("inicio m2")
    try: #tente isso
        numeros = [0,5,4]
        print(numeros[3]) 
        print("fim do acesso a lista") #como a linha acima da erro, ele não mostra isso, pois ao chegar no primeiro erro do try ele ja para e continua o codigo
    except Exception as e: #uma except (excssão) do tipo Exception (tipo mais generico das excessoes, que nos ajuda a tratar melhor os errros pois os mopstra mais claramente) tem o apelidio de "e"
        print(f'erro: {e}')
    print("fim m2")

def m1():
    print("inicio m1")
    m2();
    print("fim m2")

def main():
    print("inicio main")
    m1();
    print("fim main")


main()

'''

#Temos ainda o Finally que independente de ter erros ou não sera executado!
 #EXEMPLO:


def m2():
    print("inicio m2")
    try: #tente isso
        numeros = [0,5,4]
        print(numeros[3]) 
         
    except Exception as e: #uma except (excssão) do tipo Exception (tipo mais generico das excessoes, que nos ajuda a tratar melhor os errros pois os mopstra mais claramente) tem o apelidio de "e"
        print(f'erro: {e}')
    finally: 
        print("fim do acesso a lista") #agora o fim do acesso sera mostrado, mesmo não tendo valor no intervalo eu determinei que aquilo DEVE acontecer.
    print("fim m2")

def m1():
    print("inicio m1")
    m2();
    print("fim m2")

def main():
    print("inicio main")
    m1();
    print("fim main")


main()