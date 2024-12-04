# Función para calcular la suma de divisores propios (excluyendo al número)
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma

# Función principal para buscar números amigos en el rango [1000, 1500]
def encontrar_numeros_amigos():
    for m in range(1000, 1500):
        n = suma_divisores(m)  # Calcula la suma de divisores de m
        if n > m and n <= 1500:  # Asegura que n esté dentro del rango y sea mayor que m
            if suma_divisores(n) == m:  # Verifica si son amigos
                print(f"Par de números amigos encontrado: {m} y {n}")


encontrar_numeros_amigos()
