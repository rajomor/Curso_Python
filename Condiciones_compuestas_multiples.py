from xml.dom.expatbuilder import ElementInfo


print('===============================')
print('SENTENCIAS CONDICIONAL MULTIPLE')
print('===============================')

num_uno = int(input("CUAL ES EL NUMERO QUE DESEA CONVERTIR: "))

if   num_uno == 1:
    print("EL NUMERO ES EL UNO")
elif num_uno == 2:
    print("EL NUMERO ES EL DOS")
elif num_uno ==3:
    print('EL NUMERO ES EL TRES')
elif num_uno == 4:
    print('EL NUMERO ES EL CUATRO')
elif num_uno == 5:
    print('EL NUMERO ES EL CINCO')

else:
    print('ESTE PROGRANMA SOLO PUEDE CONVERTIR HASTRA EL NUMERO "5"')

print('FIN DEL PROGRAMA.')