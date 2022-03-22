print('Sistema para calcular el promedio de un alumno')
nombre = input('Introduzca el Nombre?: ')
matematicas = float(input(nombre + ' Cual es la calificacion de Matematicas: '))
quimica     = float(input(nombre + ' Cual es la calificacion de Quimica: '))
biologia    = float(input(nombre + ' Cual es la calificacion de biologia: '))
promedio = (matematicas + quimica + biologia) / 3
if promedio >= 6:
    print('Felicidades ', nombre, 'APROBASTE el curso con un promedio',promedio)
    print('Felicidades ', nombre, 'APROBASTE el curso con un promedio',round(promedio,2))
else:
    print('Lo sentimos ', nombre, 'has REPROBADO el curso', promedio)
    print('Lo sentimos ', nombre, 'has REPROBADO el curso', round(promedio,2))
print('Fin')