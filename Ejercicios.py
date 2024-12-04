# Escriba un programa que reciba como entrada un numero entero e indique si es o no un numero de Fibonacci

num = int(input("Por favor ingrese un número: "))

a = 0
b = 1
es_fibo = False

while a <= num:
    if a == num:
        es_fibo = True
        break
    c = a + b
    a = b
    b = c

if es_fibo:
    print(f"{num} es número de Fibonacci")
else:
    print(f"{num} no es número de Fibonacci")

