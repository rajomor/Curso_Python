("SENTENCIA CONDICIONAL SIMPLE")

print(" Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, Cual es tu nombre?: ")

matematicas = int(input(nombre + "Cual es tu calificacion de Matematicas: "))
quimica     = int(input(nombre + "Cual es tu calificacion de Quimica: "))
biologia    = int(input(nombre + "Cual es tu calificacion de Biologia: "))

promedio    = (matematicas + quimica + biologia) / 3
promedio    = int(promedio)

if promedio >= 6:
    print('Felicidades ' + nombre + ' "APROBASTES" con un promedio de: ', promedio)
print("Fin del Programa")

