# Codigo base de la lista de compras generado por Inteligencia Artificial.

def add_precios(lista_de_compras):
    total = 0
    for producto in lista_de_compras:
        total += producto['precio'] * producto['cantidad']
    return total

# Crear una lista vacía para la lista de compras
lista_de_compras = []

while True:
    # Pedir al usuario que ingrese un producto
    producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    
    # Si el usuario ingresa 'salir', terminar el bucle
    if producto.lower() == 'salir':
        break

    # Pedir al usuario que ingrese el precio del producto
    precio = float(input("Ingrese el precio del producto: "))

    # Pedir al usuario que ingrese la cantidad del producto
    cantidad = int(input("Ingrese la cantidad del producto: "))

    # Agregar el producto, su precio y su cantidad a la lista de compras
    lista_de_compras.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})

# Imprimir la lista de compras
for producto in lista_de_compras:
    print(f"Producto: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

# Imprimir el total de los precios
print(f"El total de los precios es: {add_precios(lista_de_compras)}")