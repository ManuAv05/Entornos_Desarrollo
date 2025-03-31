productos = ["manzana"]




def agregar(productos):
    producto = input("Introduce el nombre del producto: ")
    productos.append(producto)
    print(f"Producto '{producto}' agregado.")


def eliminar(productos):
    producto = input("Introduce el nombre del producto a eliminar: ")
    if producto in productos:
        productos.remove(producto)
        print(f"Producto '{producto}' eliminado.")
    else:
        print("El producto no existe en el inventario.")

def mostrar(productos):
    print("Productos en el inventario:")
    for producto in productos:
        print(f"- {producto}")
    else:
        print("Acción no válida.")



def generar_almacen(productos):
    while True:
        accion = input("¿Qué deseas hacer? (agregar/eliminar/mostrar/salir): ")
        if accion == "agregar":
            return agregar(productos)
        elif accion == "eliminar":
            return eliminar(productos)
        elif accion == "mostrar":
            return mostrar(productos)
        elif accion == "salir":
            break
        else:
            ("Caracteres no validos, intentelo de nuevo")
        

generar_almacen(productos)