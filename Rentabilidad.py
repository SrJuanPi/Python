# Programa que calcula la Rentabilidad de un Producto

def rentabilidad():
    print("¿Es este producto rentable para mí?")
    print("Escala de Rentabilidad: x/25 Valor final en porcentaje %")



    # Datos del Producto
    capital = float(input("Ingrese su capital o dinero disponible en USD: "))
    precio = float(input("Ingrese el precio del producto en USD: "))
    puntaje = 0

    durabilidad = int(input("""
    La Durabilidad está entre:

    1) 1 mes o menos
    2) más de 1 mes menos de 6 meses
    3) más de 6 meses menos de 1 año
    4) más de 1 año menos de 3 años
    5) 3 años o más

    : """))

    oferta = int(input("""
    Oferta del Producto:
                
    1) Ofrece menos que otras alternativas
    2) Ofrece un poco menos que otras alternativas
    3) Ofrece lo mismo que otras alternativas
    4) Ofrece un poco más que otras alternativas
    5) Ofrece más que otras alternativas

    : """))

    ubicacion = int(input("""
    Dónde se puede comprar el Producto

    1) En un mini market o supermercado
    2) En un centro comercial
    3) Compra Internacional
    4) En una tienda online
    5) En un local dedicado

    :"""))

    necesidad = int(input("""
    ¿De verdad necesitas este Producto?
                        
    1) No necesito este producto
    2) Es de uso ocasional
    3) Es útil pero puedo vivir sin él
    4) Es útil para mí
    5) Es una necesidad básica
                        
    :"""))



    # Definir Puntaje de Precio/Capital
    if precio < (capital*0.2):
        puntaje = 5
    elif precio < (capital*0.5):
        puntaje = 4
    elif precio == (capital*0.5):
        puntaje = 3
    elif precio > (capital*0.5) and precio < (capital*0.8):
        puntaje = 2
    elif precio > (capital*0.9) and precio < capital:
        puntaje = 1
        print("No vale la pena, te quedas pobre")
    elif precio > capital:
        print("NO VALE LA PENA TERMINARÁS ENDEUDADO")
    else:
        print("Valor no válido, por favor ingrese un valor númerico")

    # Puntaje Durabilidad
    if durabilidad == 5:
        puntaje = puntaje + 5
    elif durabilidad == 4:
        puntaje = puntaje +  4
    elif durabilidad == 3:
        puntaje = puntaje +  3
    elif durabilidad == 2:
        puntaje = puntaje +  2
    elif durabilidad == 1:
        puntaje = puntaje +  1
    else:
        print("Valor no válido, por favor ingrese un valor númerico")

    # Puntaje Oferta
    if oferta == 5:
        puntaje = puntaje + 5
    elif oferta == 4:
        puntaje = puntaje + 4
    elif oferta == 3:
        puntaje = puntaje + 3
    elif oferta == 2:
        puntaje = puntaje + 2
    elif oferta == 1:
        puntaje = puntaje + 1
    else:
        print("Valor no válido, por favor ingrese un valor númerico")

    # Puntaje Ubicación
    if ubicacion == 5:
        puntaje = puntaje + 5
    elif ubicacion == 4:
        puntaje = puntaje + 4
    elif ubicacion == 3:
        puntaje = puntaje + 3
    elif ubicacion == 2:
        puntaje = puntaje + 2
    elif ubicacion == 1:
        puntaje = puntaje + 1
    else:
        print("Valor no válido, por favor ingrese un valor númerico")

    # Puntaje Necesidad
    if necesidad == 5:
        puntaje = puntaje + 5
    elif necesidad == 4:
        puntaje = puntaje + 4
    elif necesidad == 3:
        puntaje = puntaje + 3
    elif necesidad == 2:
        puntaje = puntaje + 2
    elif necesidad == 1:
        puntaje = puntaje + 1
    else:
        print("Valor no válido, por favor ingrese un valor númerico")

    puntaje = (puntaje/30)*100


    print(f"La Rentabilidad del Producto es: {round(puntaje, 2)}%")

rentabilidad()