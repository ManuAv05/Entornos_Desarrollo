# Código inicial
def formatear_texto(texto):
    print(texto.upper())
    print(texto.lower())
    print(texto.capitalize())



def mayus(texto):
    print(texto.upper())

def minus(texto):
    print(texto.lower())

def capitalize(texto):
    print(texto.capitalize())


def Inicializar():
    texto = str(input("Introduce un texto: "))
    modo = str(input("Elige el estilo: mayuscula/miniscula/capitalize: "))

    if modo == "mayuscula":
        return mayus(texto)
    elif modo == "miniscula":
        return minus(texto)
    elif modo == "capitalize":
        return capitalize(texto)
    

Inicializar()