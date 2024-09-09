"""Q7. Escreva um algoritmo que solicita ao usuário uma temperatura em graus Celsius e a converte para graus Fahrenheit e Kelvin. Use as fórmulas Fahrenheit = Celsius * 1.8 + 32 e Kelvin = Celsius + 273.15 para realizar as conversões.
"""

temperatura_celsius = float(input("Digite a temperatura em celsius: "));

temperatura_Fahrenheit = (temperatura_celsius*1.8 +32);
temperatura_Kelvin = (temperatura_celsius+273.15);

print("essa temperatura em Fahrenheite é:", temperatura_Fahrenheit,"e em Kelvin é:", temperatura_Kelvin)