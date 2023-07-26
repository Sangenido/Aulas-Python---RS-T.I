altura1 = float(input('Digite a estatura da 1º pessoa: '))
altura2 = float(input('Digite a estatura da 2º pessoa: '))
altura3 = float(input('Digite a estatura da 3º pessoa: '))

if altura1 == altura2 or altura1 == altura3 or altura2 == altura3:
    print('Há pelo menos duas pessoas com a mesma altura: ')
elif altura1 > altura2 and altura1 > altura3:
    print(f' A pessoa mais alta tem {altura1}m.')
elif altura2 > altura1 and altura2 > altura3:
    print(f' A pessoa mais alta tem {altura2}m')
else:
    print(f' A pessoa mais alta tem {altura3}m')
