from random import shuffle


numeros = list(range(11))
print('Lista gerada:')
print(numeros)

shuffle(numeros)
print('Lista embaralhada:')
print(numeros)

print('######### Função sorted #########')
numeros_ordenados = sorted(numeros)
print('Números ordendados')
print(numeros_ordenados)

print('Lista original:')
print(numeros)

print(numeros_ordenados is numeros)
print('########## Método sort ##########')
resultado = numeros.sort()
print('Retorno do método sort')
print(resultado)
print('Lista original foi alterada, está ordenada: ')
print(numeros)
