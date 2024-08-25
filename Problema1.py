"""
Hou, Edwin			8-1021-1916
Arosemena, Miguel	8-1016-2330
Corrales, Diego		8-1001-1890
Camaño, Edward		8-1010-515
Pino, Josué			8-1012-688
"""
#InicioAlgoritmo
from math import sqrt #cargamos la libreria math para importar la funcion de raiz

#Bucle while para seguir preguntando al usuario los litros cuando ingrese un valor no valido
while True:
    try:
        litros = float(input("Ingrese la cantidad de litros a convertir: "))
        #Validar que los litros ingresados no sean negativos o cero
        if litros <= 0:
            print("El volumen ingresado debe ser un número positivo.")
            #Si se cumple la condicion este saltara al siguiente ciclo de interación sin ejecutar el resto del codigo dentro del bucle
            continue
        break #Si el valor es valido, saldra del bucle
    #Mostrara un mensaje de error, si se ingresa un valor no valido
    except ValueError:
        print("Se ha producido un error con el valor ingresado")
#Finwhile

#Bucle while para seguir preguntando al usuario la altura cuando ingrese un valor no valido  
while True:
    try:
        altura = float(input("Ingrese la altura en metros: "))
        #Validar que la altura ingresados no sean negativos o cero
        if altura <= 0:
            print("La altura ingresada debe ser un número positivo.")
            continue
        break 
    except ValueError:
        print("Se ha producido un error con el valor ingresado")
#Finwhile

#Calculo de la conversion de litros a metros cubicos
volumen = litros/1000 #1 metro cubico equivale a 0.001 litros

#Calculo del radio despejado de la formula de volumen de un cilindro
radio = sqrt(volumen/(3.14*altura)) 

#Calculo del diametro a partir del radio
diametro = radio*2 #El diametro es dos veces el radio

#Bloque para imprimir los valores del radio y el diametro
print("El radio del recipiente cilindrico es {:.2f} metros".format(radio))
print("El diametro de la base del recipiente cilindrico es {:.2f} metros".format(diametro))
#FinAlgoritmo