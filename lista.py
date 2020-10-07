lista = ['inicio', 2, '3.5', 4.0, 5.0, 'fin']
print(lista)

print('1. Tamaño de la lista: ', len(lista))

print('2. Tamaño de la lista multiplicado por su segundo elemento: ',
      len(lista) * lista[1])

print('3. Producto del segundo elemento de la lista por el tercero: ',
      lista[1] * lista[2])

print('4. ¿Está 2 en la lista? ', 2 in lista, '¿y 2.0?', 2.0 in lista)

print('5. Eliminar el primer elemento de la lista')
lista.pop(0)
print('  Nueva lista:', lista)

print('6. Eliminar dos últimos elementos simultáneamente')
del lista[-2:]
print('  Nueva lista:', lista)

print('7. ¿Está vacía la lista?', not lista)
lista.append('nuevo ultimo')
print("8. Añadir el elemento 'nuevo ultimo' a la lista:", lista)
