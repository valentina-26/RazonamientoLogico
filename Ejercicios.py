# Escriba un programa que muestre los m primeros numeros de Fibonacci,donde m es un numero ingresado por el usuario:

m = int(input("Por favor inngrese m: "))

a = 0
b = 1

if m >= 1:
    print(a, end=" ")
if m >= 2:
    print(b, end=" ")

for i in range(2, m):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

print()


