# Código inicial
a= 5
b = 8
def suma(a,b):
    print(a+b)
   

def resta(a,b):
    print(a-b)

def multiplicacion(a,b):
    print(a*b)

def division(a,b):
    print(a/b)

def calculadora():
    opcion = (int(input("Ingrese un numero del 1 al 4, siendo 1 suma, 2 resta, 3 multiplicacion, 4 division: ")))
    if opcion == 1:
        return suma
    elif opcion == 2:
        return resta
    elif opcion == 3:
        return multiplicacion
    elif opcion == 4:
        return division

calculadora()
