while 1:
    try:
        hours = float(input("Insert Hours (Int): "))

    except ValueError:
        print("Insert an integer or float number.")

    else: break
days = hours/24
print(f"days = {days}")