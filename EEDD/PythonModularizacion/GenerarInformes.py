# Código inicial
def generar_informe(ventas):
    print("---- Informe de Ventas ----")
    total = 0
    for producto, cantidad in ventas.items():
        total += cantidad
        print(f"{producto}: {cantidad} unidades")
    print(f"Total de ventas: {total} unidades")


def printVentas():
    print("---- Informe de Ventas ----")


def bucle(ventas):
    total = 0
    for producto, cantidad in ventas.items():
        total += cantidad
        print(f"{producto}: {cantidad} unidades")

def print_Total(total):
    print(f"Total de ventas: {total} unidades")


def generar_informe(ventas, total):
    printVentas()
    bucle(ventas)
    print_Total(total)