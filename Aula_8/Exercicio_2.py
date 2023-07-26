n1 = int(input('Digite o primeiro número positivo: '))

n2 = int(input('Digite o segundo número positivo: '))

print('\n 1 - Média ponderada, com pesos 2 e 3,respectivamente')
print('2 - Quadrado da somo dos 2 números')
print('3 - Cubo do menor número')

menu = int(input('Digite uma das opções:'))

if menu < 1 or menu > 3:
    print('\n Opção Inválida!')

elif menu == 1:
    valor = (n1*2 + n2*3)/5
    print(f'A média ponderada calculada é: {valor:.2f}.')

elif menu == 2:
    quadrado = (n1+n2)**2
    print(f'O quadrado da soma dos 2 números é: {quadrado:.2f}.')

else:
    if n1 < n2:
        cubo = n1**3
        print(f'{n1:.2f} é menor e o seu cubo é {cubo:.2f}.')
    elif n1 > n2:
        cubo = n2**3
        print(f'{n2:.2f} é menor numero e o seu cubo é {cubo:.2f}.')
    else:
        n1 == n2
        cubo = n1**3
        print(f'Os numeros sao iguais,e o seu cubo é {cubo:.2f}')
