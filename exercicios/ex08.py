"""Q9. Área de um Círculo: Escreva um algoritmo que solicita ao usuário o raio de um círculo, depois calcula e exibe a área do círculo. A fórmula para calcular a área de um círculo é área = π x raio^2. Você pode usar a aproximação de 3.1416 para π.
"""

raio = float(input("Digite o raio do círculo: "));
pi = 3.1416;
area = pi*(raio*raio);
area_arredondada = round(area,2)

print("a área do circulo é de aproximadamente:", area_arredondada)
