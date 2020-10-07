cadena = "Pelo largo castaño, ojos cafés"

print('1.', len(cadena))
print('2.', cadena[:5])
print('3.', cadena[-7:])
# 4. de los 5 primeros, los que ocupan posiciones pares
print('4.', cadena[:5:2])
# 5. de los ultimos 13, los de posiciones impares
print('5.', cadena[-13::3])
print('6.', cadena[::3].upper())
print('7.', cadena[4:17:2])
print('8.', 'x' in cadena.lower() or ('o' in cadena or 'O' in cadena))
