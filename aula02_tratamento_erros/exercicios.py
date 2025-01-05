import numpy as np

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
soma_numeros = numero1 + numero2

print(f"A soma dos dois números do usuário é {soma_numeros}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_usuario = int(input('Digite um número: '))
numero_calculado = numero_usuario % 5
print(f"O resto da divisão de {numero_usuario} por 5 é {numero_calculado}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
multiplicacao_numeros = numero1 * numero2
print(f"A Multiplicação dos dois números do usuário é {multiplicacao_numeros}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
divisao_inteira = numero1 // numero2
print(f"A Divisão inteira dos dois números do usuário é {divisao_inteira}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_usuario = int(input('Digite um número inteiro: '))
numero_quadrado = numero_usuario ** 2
print(numero_quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
n1 = float(input('Digite um número decimal: '))
n2 = float(input('Digite outro número decimal: '))
print(f"A soma dos dois números decimais é {n1 + n2}")


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
n1 = float(input('Digite um número decimal: '))
n2 = float(input('Digite outro número decimal: '))
media_usuario = (n1 + n2) / 2
print(f"A média é {media_usuario}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_base = float(input('Digite um número base para potência: '))
expoente = int(input('Digite um expoente: '))
print(f"O resultado de {numero_base} elevado a {expoente} é {numero_base ** expoente}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input('Digite uma temperatura em graus Celsius: '))
g_fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} graus Celsius equivalem a {g_fahrenheit:.2f} graus Fahrenheit")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input('Digite o raio do circulo: '))
area = np.pi * raio ** 2
print(f'A área do círculo é: {area}')


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string_usuario = input('Digite qualquer coisa').upper()
print(string_usuario)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_usuario = input('Digite seu nome').lower()
print(nome_usuario)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase_usuario = input('Digite uma frase').strip()
print(frase_usuario)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input('Digite uma data no formato dd/mm/aaaa: ')
data_separada = data.split('/')

print(f'Dia: {data_separada[0]}\nMês: {data_separada[1]}\nAno: {data_separada[2]}')


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
