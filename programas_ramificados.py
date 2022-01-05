def run():
    print('Este programa evalua las edades de dos personas y responde quién es mayor...\n')
    person_1 = input("Escribe el nombre de la primera persona >>>")
    age_1 = int(input("Escribe su edad utilizando solo números >>>"))
    person_2 = input("Escribe el nombre de la segunda persona >>>")
    age_2 = int(input("Escribe su edad utilizando solo números >>>"))

    if age_1 > age_2:
        print(person_1, 'es mayor que', person_2)
    elif age_1 < age_2:
        print(person_1, 'es menor que', person_2)
    else:
        print(person_1, 'tiene la misma edad que', person_2)
    

if __name__ == '__main__':
    run()