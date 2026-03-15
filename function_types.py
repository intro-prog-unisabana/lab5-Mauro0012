def list_shift(lista: list[float], valor: float):
    for i in range(len(lista)):
        lista[i] += valor

def calc_avg(x: list[float]) -> float:
    return (sum (x)/len(x))

def print_normalized(lst: list[float]):
    print(lst)
datos = [2.0, 4.0, 6.0, 8.0]

prom = calc_avg(datos)         
list_shift(datos, -9)       
print_normalized(datos) 