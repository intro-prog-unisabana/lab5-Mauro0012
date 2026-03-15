def obtener_precio_usuario():
    a=input("Enter the item's price:\n")
    return float(a)
if __name__ == "__main__":
    precio = obtener_precio_usuario()
    print(precio)