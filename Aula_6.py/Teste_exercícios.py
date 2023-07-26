print('################################################################')
print('                    Cáculo de Grandezas Elétricas               ')
print('################################################################')
print('1. Tensão(v)')
print('2. Resistência(ohm)')
print('3. Corrente(ampere)')

opcao = int(input('Digite a opção: '))

if opcao == 1:
    R = float(input('O valor da resistência é: '))
    I = float(input('O valor da corrente é: '))
    valor = R*I
elif opcao == 2:
    U = float(input('O valor da tensão é: '))
    I = float(input('O valor da corrente é: '))
    valor = U/I
elif opcao == 3:
    U = float(input('O valor da tensão é: '))
    R = float(input('O valor da resistência é: '))
    valor = U/R
else:
    print('Opção Inválida')
print('O valor da grandeza escolhida será: {}'.format(valor))
