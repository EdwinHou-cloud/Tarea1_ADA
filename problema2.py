"""
Hou, Edwin			8-1021-1916
Arosemena, Miguel	8-1016-2330
Corrales, Diego		8-1001-1890
Camaño, Edward		8-1010-515
Pino, Josué			8-1012-688
"""

#InicioAlgoritmo
from math import sqrt, cos, pi #cargamos la libreria math para importar la funcion de raiz, de coseno y la constante pi

#Bucle while para seguir preguntando al usuario el primer lado cuando ingrese un valor no valido
while True:
    try:
        lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
        #Validar que el primer lado ingresado no sea negativo o cero
        if lado1 <= 0:
            print("Las longitudes de los lados deben ser números positivos.")
            #Si se cumple la condicion este saltara al siguiente ciclo de interación sin ejecutar el resto del codigo dentro del bucle
            continue
        break #Si el valor es valido, saldra del bucle
    #Mostrara un mensaje de error, si se ingresa un valor no valido
    except ValueError:
        print("Se ha producido un error con el valor ingresado")
#Finwhile

#Bucle while para seguir preguntando al usuario el segundo lado cuando ingrese un valor no valido
while True:
    try:
        lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
        #Validar que el segundo lado ingresado no sea negativo o cero
        if lado2 <= 0:
            print("Las longitudes de los lados deben ser números positivos.")
            continue
        break
    except ValueError:
        print("Se ha producido un error con el valor ingresado")
#Finwhile

#Bucle while para seguir preguntando al usuario el angulo lado cuando ingrese un valor no valido
while True:
    try:
        angulo = float(input("Ingrese el ángulo entre los dos lados: "))
        if angulo <= 0 or angulo >= 180:
            print("El ángulo debe estar entre 0 y 180 grados.")
            continue
        break
    except ValueError:
        print("Se ha producido un error con el valor ingresado")
#Finwhile

#Calculo de la conversion del angulo en grados a radianes, dado que la funcion cos espera un angulo en radianes
anguloRad = angulo*(pi/180)

#Calculo del tercer lado
lado3 = sqrt(lado1**2 + lado2**2 - 2*lado1*lado2*cos(anguloRad)) #Ecuacion para calcular el tercer lado

#Imprimir el valor del tercer lado
print("La longitud del tercer lado del triángulo es {:.2f}".format(lado3))
#FinAlgoritmo