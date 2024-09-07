# Facilitar el manejo del dinero a la hora de comprar en el super

# Pedimos el dinero para gastar
# En caso de no ingresar un número, manejamos una excepción
while True:
    try: dinero_disponible = float(input("Ingrese el dinero que dispone para gastar: "))
    except: print("Ingrese un número")
    else: break

lista = [] # Lista final de compras con todos los detalles.

# addr los precios a medida que se añaden
def add_precios(lista):
    total = 0
    for producto in lista:
        total += producto['precio'] * producto['cantidad']
    return total

# Añadimos tantos productos como el usuario lo requiera.
while True:
    producto = input("Nombre del producto (o salir para continuar): ")
    if producto.lower() == "salir":
        break

    while True: # Otro manejo de excepciones
        try: precio = int(input("Precio por unidad: "))
        except: print("Ingrese un número")
        else: break
    while True:
        try: cantidad = int(input("Cantidad de unidades: "))
        except: print("Ingrese un número")
        else: break

    # Se añaden los datos del producto a la lista
    lista.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})
    # Se addn los precios a medida que se añaden para llevar la cuenta
    print(f"Precio Total: {add_precios(lista)}")


# Mostramos la lista completa de productos con sus detalles.
for producto in lista:
    print(f"\nProducto: {producto['nombre']}\nPrecio: {producto['precio']}\nCantidad: {producto['cantidad']}")


# Verificamos si el usuario puede pagar o no la compra
if add_precios(lista) <= dinero_disponible:
    print(f"\nEl precio total es: {add_precios(lista)} y te sobran {abs(dinero_disponible - add_precios(lista))}")

elif add_precios(lista) > dinero_disponible:
    print(f"\nNo tienes para pagarlo, te faltan {abs(dinero_disponible - add_precios(lista))}")




# Completado con Éxito! como recomendación: agregar un sistema que te permita quitar productos (ya sea enteros o por cantidades)