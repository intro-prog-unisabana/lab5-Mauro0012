import math
import os

directorio_actual = os.getcwd()
print("Current working directory:", directorio_actual)
entero=int(input("Enter an integer: "))
log=math.log2(entero)
print("Log base 2 of 10 is:", log)
print("Floor:", math.floor(log))
print("Ceiling:", math.ceil(log))