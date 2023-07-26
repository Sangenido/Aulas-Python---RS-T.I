print(' ********** Tabela Verdade *******')
print(' 1- Operador AND')
print(' 2- Operador OR')
print(' 3- Operador NOT')
op = int(input('Escolha uma opção: '))
if op < 1 or op > 3:
    print('Opção Inválida')
elif op == 3:
    operador = int(input('Informe o bit:'))
    print(f'NOT {operador} = {not (operador)}')
else:
    operador1 = int(input('Informe o primeiro bit: '))
    operador2=int(input('Informe o segundo bit: '))
    if op == 1:
        print(f'{operador1} AND {operador2} = {operador1 and operador2}')
    else:
        print(f'{operador1} AND {operador2} = {operador1 or operador2}')
