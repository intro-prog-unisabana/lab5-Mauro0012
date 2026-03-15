from random import seed, randint
seed(123)
start=int(input("Enter the start value:\n"))
end=int(input("Enter the end value:\n"))
print(f"Generated random number: {randint(start, end)}")


