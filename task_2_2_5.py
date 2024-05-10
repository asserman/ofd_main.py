while True:
    temp_inp = float(input("темпереатура в градусах (C)--> "))
    temp_c = f"{temp_inp:.1f}"
    if (temp_inp < 10):
        print(f"you entered {temp_c} degres. It`s cold!")
    else:
        if  (temp_inp < 25):
            print(f"you entered {temp_c} degres. It`s cool!")
        else:
            if  (temp_inp > 25):
                print(f"you entered {temp_c} degres. It`s hot!")
