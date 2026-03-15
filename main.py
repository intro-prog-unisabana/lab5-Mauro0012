from utils_calc import *
while True:
    operacion=input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):").lower()
    if operacion==("add"):
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        suma=add(a, b)
        print("The result is:", suma)
    elif operacion==("subtract"):
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        resta=sub(a, b)
        print("The result is:", resta)
    elif operacion==("multiply"):
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        multi=multiply(a, b)
        print("The result is:", multi)
    elif operacion==("divide"):
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        div=divide(a, b)
        if b==0:
            print(f"{div}")
        else:
            print("The result is:", div)
    elif operacion==("exponent"):
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        exp=exponent(a, b)
        print("The result is:", exp)
    elif operacion==("modulo"):
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        mod=modulo(a, b)
        if b==0:
            print(f"{mod}")
        else:
            print("The result is:", mod)
    elif operacion==("floor_divide"):
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        f_d=floor_divide(a, b)
        if b==0:
            print(f"{f_d}")
        else:
            print("The result is:", f_d)
    elif operacion==("absolute"):
        a=float(input("Enter the number:"))
        absol=absolute(a)
        print("The result is:", absol)
    elif operacion==("exit"):
        break
    else:
        print("Invalid option!")