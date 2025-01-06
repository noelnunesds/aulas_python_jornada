import re

def validar_nome(nome):
   
    if nome.isdigit():
        raise ValueError('Você digitou seu nome errado. Não deve conter apenas números.')
    elif len(nome.strip()) == 0:
        raise ValueError('Você não digitou nada ou apenas espaços.')
    elif not re.match(r"^[a-zA-ZÀ-ÿ\s]+$", nome):
        raise ValueError('O nome não deve conter caracteres especiais.')
    return nome

def validar_salario(salario):
    if salario <= 0:
        raise ValueError('Erro: Salário não pode ser 0 ou negativo.')
    return salario

def validar_bonus(bonus):
    if bonus > 1:
        bonus /= 100
    elif bonus < 0:
        raise ValueError('O valor do bônus não pode ser negativo.')
    return bonus


try:
    # Validação do nome
    nome = input('Qual é o seu nome? ')
    nome = validar_nome(nome)

    # Validação do salário
    salario = float(input('Qual é o valor do seu Salário? '))
    salario = validar_salario(salario)

    # Validação do bônus
    bonus = float(input('Digite o valor do seu bônus: '))
    bonus = validar_bonus(bonus)

    # Cálculo do valor do bônus
    BONUS_2024 = 1000
    valor_bonus = BONUS_2024 + salario * bonus

    # Saída final
    print(f'\nUsuário: {nome}\nSalário: R$ {salario:.2f}\nValor do bônus: R$ {valor_bonus:.2f}')

except ValueError as e:
    print(f'Erro: {e}')
except Exception as e:
    print(f'Erro inesperado: {e}')