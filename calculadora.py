numero_1 = 0
numero_2 = 0

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def potencia(a, b):
    return pow(a, b)

def valida_es_cero(numero):
    return numero == 0 or numero == 0.0

def captura_numeros():
    numero_1 = input('Ingresa el primer número: ')
    numero_2 = input('Ingresa el segundo número: ')

def menu():
    return 1

if __name__ == '__main__':
    menu()
