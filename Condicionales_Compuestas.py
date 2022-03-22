("SENTENCIA CONDICIONAL COMPUESTAS")

print(" Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, Cual es tu nombre?: ")

matematicas = int(input(nombre + "Cual es tu calificacion de Matematicas: "))
quimica     = int(input(nombre + "Cual es tu calificacion de Quimica: "))
biologia    = int(input(nombre + "Cual es tu calificacion de Biologia: "))

promedio    = (matematicas + quimica + biologia) / 3
promedio    = (promedio)

if promedio >= 6:
    print('Felicidades ' + nombre + ' "APROBASTES" con un promedio de: ', promedio)
    print('Felicidades ' + nombre + ' "APROBASTES" con un promedio de: ', round(promedio,2))
else:
    print('Lo Sentimos ' + nombre + ' "NO APROBASTES " con un promedio de: ', promedio)
    print('Lo Sentimos ' + nombre + ' "NO APROBASTES " con un promedio de: ', round(promedio,2))


print("Fin del Programa")

