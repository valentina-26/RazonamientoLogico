
multiplicador = int(input("Por favor ingrese el multiplicador: "))
multiplicando = int(input("Por favor ingrese el multiplicando: "))

resultado = 0
while multiplicador > 1:
    if multiplicador % 2 != 0:
        resultado += multiplicando
    multiplicando *= 2
    multiplicador //= 2

resultado += multiplicando
print(f"El resultado es: {resultado}")