# Calculadora de Indice de Masa Corporal

def imc():
    print("Calculadora IMC")

    # Datos del usuario
    sexo = input("Ingrese su sexo, si es Hombre (H) o si es Mujer (M): ")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    # Calculando el IMC
    imc = (peso / (altura*2))
    print(f"Su índice de masa corporal es: {imc}")

    if sexo.lower() == "h":
        if imc >= 19 and imc <= 24:
            print("Está en un peso Saludable")
        elif imc < 19:
            print("Estas por debajo de tu peso ideal, trata de comer más")
        elif imc > 24 and imc < 29.1:
            print("Tienes sobrepeso, trata de hacer ejercio regularmente")
        elif imc > 29 and imc < 39:
            print("Tienes obesidad, ve a un médico, cambia tu dieta y has ejercicio.")
        elif imc >= 39:
            print("Necesitas ayuda urgentemente, ve al médico ya")


    if sexo.lower() == "m":
        if imc > 18 and imc <= 23:
            print("Estás en un peso Saludable")
        elif imc <= 18:
            print("Estas por debajo de tu peso ideal, trata de comer más")
        elif imc > 23 and imc < 28.1:
            print("Tienes sobrepeso, trata de hacer ejercio regularmente")
        elif imc > 28 and imc < 38:
            print("Tienes obesidad, ve a un médico, cambia tu dieta y has ejercicio.")
        elif imc >= 38:
            print("Necesitas ayuda urgentemente, ve al médico ya")