ncamisa = float(input('Informe quantas camisas deseja comprar: '))
valor = 78.50
total = ncamisa * valor
if ncamisa <= 5:
    total = total * (1-3/100)
else:
    if ncamisa < 10:
        total = total * (1-5/100)
    else:
        total = total * (1-7/100)

print(f'Valor final: R$ {total:.2f}')
