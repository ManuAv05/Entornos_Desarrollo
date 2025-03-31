# Código inicial
def calcular_estadisticas(numeros):
    promedio = sum(numeros) / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    print(f"Promedio: {promedio}, Máximo: {maximo}, Mínimo: {minimo}")

numeros = 2,5,9,8

def promedio(numeros):
    promedio = sum(numeros) / len(numeros)
    print(promedio)

def maximo(numeros):
    maximo = max(numeros)
    print(maximo)

def minimo(numeros):
    minimo = min(numeros)
    print(minimo)

def Inicializar(numeros):
    numero = int(input("Ingrese un numero  1:promedio/2:maximo/3:minimo: "))
    if numero == 1:
        return promedio(numeros)
    elif numero == 2:
        return maximo(numeros)
    elif numero == 3:
        return minimo(numeros)
    

Inicializar(numeros)