
cantidad_universidades = int(input("Ingrese la cantidad de universidades: "))


universidades_aceptan = 0
universidades_rechazan = 0
universidades_empate = 0


for i in range(cantidad_universidades):
    print(f"\nUniversidad {i + 1}:")
    nombre_universidad = input("Por favor ingrese el nombre de la universidad: ")

    # Contadores de votos por tipo
    votos_a = 0  # Aceptar
    votos_r = 0  # Rechazar
    votos_n = 0  # Nulo
    votos_b = 0  # Blanco

    print("Ingrese los votos (A/R/N/B). Ingrese 'X' para terminar:")
    while True:
        voto = input("Voto: ").upper()
        if voto == 'X':
            break
        elif voto == 'A':
            votos_a += 1
        elif voto == 'R':
            votos_r += 1
        elif voto == 'N':
            votos_n += 1
        elif voto == 'B':
            votos_b += 1
        else:
            print("Voto inválido. Intente de nuevo.")


    print(f"\nResultados de {nombre_universidad}:")
    print(f"Aceptar (A): {votos_a}")
    print(f"Rechazar (R): {votos_r}")
    print(f"Nulo (N): {votos_n}")
    print(f"Blanco (B): {votos_b}")


    if votos_a > votos_r:
        universidades_aceptan += 1
    elif votos_r > votos_a:
        universidades_rechazan += 1
    else:
        universidades_empate += 1


print("\nResultados finales:")
print(f"Universidades que aceptan: {universidades_aceptan}")
print(f"Universidades que rechazan: {universidades_rechazan}")
print(f"Universidades con empate: {universidades_empate}")
