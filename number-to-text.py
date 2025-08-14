numero = input("Enter a number: ")

palabras = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    }
categorias = {
    1: "units",
    2: "tens",
    3: "hundreds",
    4: "thousands",
    5: "ten thousands",
    6: "hundred thousands",
    7: "millions",
    8: "ten millions",
    9: "hundred millions",
    10: "billions",
    11: "ten billions",
    12: "hundred billions",
    13: "trillions",
    14: "ten trillions",
    15: "hundred trillions",
    16: "quadrillions",
    17: "ten quadrillions",
    18: "hundred quadrillions",
    19: "quintillions",
}

# Funcion para convertir cada digito a su palabra correspondiente
def valor_posicional():
    digitos = []
    for i in numero:
        digitos.append(int(i))
    valor_posicional = digitos[::-1]
    return valor_posicional

def convertir_unidad_a_texto(vp):
    texto = ""
    for i in len(vp):
        texto += vp[i-1] + " " + categorias[i] + " "
    return texto

valor_posicional = valor_posicional()
convertir_unidad_a_texto(valor_posicional)