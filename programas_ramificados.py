def run():
    num_1 = int(input('Escribe un número entero: '))
    num_2 = int(input('Escribe otro número entero: '))

    if num_1 > num_2:
        print(num_1, 'es mayor que', num_2)

if __name__ == '__main__':
    run()