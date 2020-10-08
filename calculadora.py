# Calculadora con opciones aritméticas básicas
# Sistemas programables 12:15 - 13:55
# Jéssica Ramírez Sánchez
# 07 Octubre 2020

def es_cero(numero):
    return numero == 0 or numero == 0.0

def es_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        print('Por favor, escribe un número')
        return False

def operaciones(opcion, numero1, numero2):
    simbolos = ['+', '-', '*', '/', '^']

    if es_cero(numero2) and opcion == 4:
        print('No se puede dividir entre cero')
        menu()

    switcher = {
        1: numero1 + numero2,
        2: numero1 - numero2,
        3: numero1 * numero2,
        4: numero1 / numero2,
        5: numero1 ** numero2
    }

    print(f'El resultado de {numero1} {simbolos[opcion - 1]} {numero2} = {switcher[opcion]}')
    menu()

def captura_numero():
    numero = float(input('Ingresa un número: '))
    while not es_numero(numero):
        numero = float(input('Ingresa un número: '))
    return numero

def menu():
    print("""
        Elige una opción del menú:
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Potencia
        6. Salir
    """ )

    opcion = int(input('> '))
    while not es_numero(opcion):
        opcion = int(input('> '))

    if opcion == 6:
        exit()

    numero1 = captura_numero()
    numero2 = captura_numero()
    operaciones(opcion, numero1, numero2)

if __name__ == '__main__':
    menu()
