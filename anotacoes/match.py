#o match é usado para evitarmos o uso ecessivo de estruturas condicionais. 

#ex:
rodadas = 0
while (rodadas != 13):
    mes = int(input("digite o mês do seu nascimento ou 13 para parar: "))

    match mes:  #avalie mes
        case 1: #caso seja 1
            print("Janeiro");
            rodadas = mes
        case 2: #caso seja 2
            print("Fevereiro");
            rodadas = mes
        case 3: #caso seja 3
            print("Março");
            rodadas = mes
        case 4: #caso seja 4
            print("Abril");
            rodadas = mes
        case 5: #caso seja 5
            print("Maio");
            rodadas = mes
        case 6: #caso seja 6
            print("Junho");
            rodadas = mes
        case 7: #caso seja 7
            print("Julho");
            rodadas = mes
        case 8: #caso seja 8
            print("Agosto");
            rodadas = mes
        case 9: #caso seja 9
            print("Setembro");
            rodadas = mes
        case 10: #caso seja 10
            print("Outubro");
            rodadas = mes
        case 11: #caso seja 11
            print("Novembro");
            rodadas = mes
        case 12: #caso seja 12
            print("Dezembro");
            rodadas = mes
        case 13: #caso seja 13
            print("fim de jogo")
            rodadas = mes
            #finaliza, pois a condição do while foi atingida.







    