ncamisa=int(input('Número de camisas: '))
valor= 78.50
valorfinal=ncamisa*valor
if ncamisa <5:
    valorfinal=valorfinal * (1-3/100)
elif ncamisa <10:
    valorfinal=valorfinal * (1-5/100)
else:
    valorfinal  = valorfinal * (1-7/100) 

print(f'valor final: R$ {valorfinal:.2f}')
