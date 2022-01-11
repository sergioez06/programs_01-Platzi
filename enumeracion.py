import math

def run():
    numero = int(input('Escribe un número entero: '))
    respuesta = math.sqrt(numero)

    if (math.sqrt(numero) % 1 == 0):
        print(f'La raiz cuadrada de {numero} es {respuesta}')
    else:
        print(f'{numero} no tiene raiz cuadrada exacta')

if __name__ == '__main__':
    run()