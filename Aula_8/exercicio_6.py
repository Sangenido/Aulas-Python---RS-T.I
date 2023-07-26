sobrenome = input('Informe o sobrenome do apresentador: ')

if sobrenome.upper() == 'PINHEIRO' or sobrenome.upper() == 'ARAÚJO':
    print('Bom dia Nação!')
elif sobrenome.upper() == 'BONNER' or sobrenome.upper() == 'VASCONCELOS':
    print('Jornal Brasileiro!')
else:
    print('Apresentador desconhecido!')
