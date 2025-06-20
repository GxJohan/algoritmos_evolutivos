# Padres del ejemplo (con 8 elementos)
padre_1 = [1, 2, 3, 4, 5, 6, 7, 8]
padre_2 = [8, 7, 6, 5, 4, 3, 2, 1]

# Puntos de cruce (índices)
inicio_cruce = 3
fin_cruce = 6  # Segmento de cruce: posiciones 3, 4, 5

# Paso 1: Copiar el segmento del Padre 2 al Hijo 1
hijo_1 = [-1] * len(padre_1)
hijo_1[inicio_cruce:fin_cruce] = padre_2[inicio_cruce:fin_cruce]

# Crear el mapeo entre los genes intercambiados
mapeo = {}
for i in range(inicio_cruce, fin_cruce):
    mapeo[padre_1[i]] = padre_2[i]
    mapeo[padre_2[i]] = padre_1[i]  # mapeo bidireccional

# Paso 2: Completar el resto del hijo con los genes del Padre 1
for i in range(len(padre_1)):
    if i >= inicio_cruce and i < fin_cruce:
        continue  # Saltar el segmento de cruce

    gen = padre_1[i]
    
    # Resolver conflictos: si el gen ya está en el hijo, usar el mapeo
    while gen in hijo_1[inicio_cruce:fin_cruce]:
        gen = mapeo[gen]  # usar el mapeo hasta encontrar uno válido

    hijo_1[i] = gen

# Mostrar resultados
print("Padre 1:", padre_1)
print("Padre 2:", padre_2)
print("Hijo 1: ", hijo_1)
