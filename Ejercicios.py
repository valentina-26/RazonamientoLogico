# Escriba un programa que reciba como entrada un numero entre n,y entregue como salida el n-enesimo numero de fibonacci

def fibonacci_n(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Entrada del usuario
n = int(input("Ingrese n: "))
print(f"F{n} = {fibonacci_n(n)}")


