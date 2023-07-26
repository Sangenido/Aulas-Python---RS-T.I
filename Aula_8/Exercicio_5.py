print('_*'*20)
print('1- Programador de sistemas')
print('2 - Analista de Sistemas')
print('3 - Analista de Banco de Dados')
print('_*'*20)

salario = float(input('Digite o salario do colaborador:R$ '))
cargo = int(input('Digite o cargo do colaborador: '))
if cargo < 1 or cargo > 3:
    print('Cargo Inválido!')
elif cargo == 1:
    '''Acréscimo de 30% sobre o salário atual. Mesmo que:
    salario = salario * 1.3 ou 
    salario = salario + salario * 0.3'''
    salario *= 1.3
    print(f'Novo salário: R$ {salario:.2f}')
elif cargo == 2:
    '''Acréscimo de 20% sobre o salário atual. Mesmo que:
    salario = salario * 1.2 ou 
    salario = salario + salario * 0.2'''
    salario *= 1.2
    print(f'Novo salário: R$ {salario:.2f}')
else:
    '''Acréscimo de 15% sobre o salário atual. Mesmo que:
    salario = salario * 1.15 ou 
    salario = salario + salario * 0.15'''
    salario *= 1.15
    print(f'Novo salário: R$ {salario:.2f}')
