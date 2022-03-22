print('=========')
print('CONVERSOR')
print('=========\n')

print('MENU DE OPCIONES: \n')
print('PRESIONA 1 PARA CONVERTIR DE NUMERO A PLABRA')
print('PRESIONA 22 PARA CONVERTIR DE PLABRA A NUMERO')

opcion = int(input('CUAL ES TU OPCION?: '))

if opcion == 1:
    print('\n CONVERSIOR DE NUMERO A PALABRA. \n')

    opcion_uno = int(input('Cual es el numero que desea convertir en palabra'))

    if   opcion_uno == 1:
        print('EL NUMERO ES EL UNO')
    elif opcion_uno == 2:
        print('EL NUMERO ES EL DOS')
    elif opcion_uno == 3:
        print('EL NUMERO ES EL TRES')
    elif opcion_uno == 4:
        print('EL NUMERO ES EL CUATRO')
    elif opcion_uno == 5:
        print('EL NUMERO ES EL CINCO')
    else:
        print('EL NUMERO REGISTRADO NO ESTA DISPONIBLE')

elif opcion == 2:
    print('\n CONVERSIOR DE PALABRA A NUMERO. \n')

    opcion_dos = input('CUAL ES LA PALABRA QUE DESEA CONVERTIR EN NUMERO: ')
    opcion_dos = opcion_dos.lower()

    if   opcion_dos == 'uno':
        print('EL NUMERO ES EL 1')
    elif opcion_dos == 'dos':
        print('EL NUMERO ES EL 2')
    elif opcion_dos == 'tres':
        print('EL NUMERO ES EL 3')
    elif opcion_dos == 'cuatro':
        print('EL NUMERO ES EL 4')
    elif opcion_dos == 'cinco':
        print('EL NUMERO ES EL 5')
    else:
        print('EL NUMERO REGISTRADO NO ESTA DISPONIBLE')

else:
    print('Opcion no disponible')
print('Fin del Programa')

