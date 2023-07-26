n1 = int(input('Informe um número inteiro positivo: '))
if n1 % 2 == 0:
    n1 = n1**2
    print(f'O número é par e ao quadrado é: {n1:.2f}')
else:
    n1 = n1**3
    print(f'O número é ímpar e ao cubo é: {n1:.2f}')
