# Cálculo de bônus com entrada do usuário

nome = input('Qual é o seu nome? ')
salario = float(input('Qual é o valor do seu Salário? '))
bonus = float(input('Digite o valor do seu bônus: '))
BONUS_2024 = 1000

valor_bonus = BONUS_2024 + salario * bonus

print(f'Usuário: {nome}\nSalário: {salario}\nValor do bonus: {valor_bonus}')