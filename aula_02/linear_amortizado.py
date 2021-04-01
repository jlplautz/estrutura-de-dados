

lista_de_numeros=list(range(10))
print(id(lista_de_numeros))
print(id(lista_de_numeros[0]))
print(id(lista_de_numeros[1]))
print(id(lista_de_numeros[2]))
lista_de_numeros.append(10)
print(id(lista_de_numeros))