try:
    numero1 = int(input('Digite um número inteiro: '))
    numero2 = int(input('Digite outro número inteiro: '))
    divisao_inteira = numero1 // numero2
    print(f"A Divisão inteira dos dois números do usuário é {divisao_inteira}")
except ZeroDivisionError:
    print('Interger division or modulo by zero')