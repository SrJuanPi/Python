# Body Mass Index Calculator

def bmi():
    print("BMI Calculator")

    # Datos del usuario
    sex = input("Enter your gender, if you are Male (M) or if you are Female (F): ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    # Calculando el bmi
    bmi = (weight / (height*2))
    print(f"Your body mass index is: {bmi}")

    if sex.lower() == "h":
        if bmi >= 19 and bmi <= 24:
            print("You are in a healthy weight")
        elif bmi < 19:
            print("You are below your ideal weight, try to eat more")
        elif bmi > 24 and bmi < 29.1:
            print("You are overweight, try to exercise regularly")
        elif bmi > 29 and bmi < 39:
            print("You are obese, go to a doctor, change your diet and exercise.")
        elif bmi >= 39:
            print("You need help urgently, go to the doctor now")


    if sex.lower() == "m":
        if bmi > 18 and bmi <= 23:
            print("You are in a healthy weight")
        elif bmi <= 18:
            print("You are below your ideal weight, try to eat more")
        elif bmi > 23 and bmi < 28.1:
            print("You are overweight, try to exercise regularly")
        elif bmi > 28 and bmi < 38:
            print("You are obese, go to a doctor, change your diet and exercise.")
        elif bmi >= 38:
            print("You need help urgently, go to the doctor now")