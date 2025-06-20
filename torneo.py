import random

# Definir los individuos y sus fitness
individuos = {
    "A": 85,
    "B": 45,
    "C": 70,
    "D": 20,
    "E": 60,
    "F": 90
}

def seleccion_por_torneo(individuos, num_torneos=3):
    """
    Función que simula un proceso de selección por torneo.
    
    Parámetros:
    - individuos: Diccionario con el nombre del individuo y su fitness.
    - num_torneos: Número de torneos a realizar (por defecto 3).

    Retorna:
    - Una lista con los ganadores de cada torneo.
    """
    ganadores = []

    # Convertir los items del diccionario a una lista para usar random.sample()
    individuos_lista = list(individuos.items())

    # Para cada torneo, realizamos el proceso de selección
    for i in range(num_torneos):
        # Seleccionar aleatoriamente dos individuos
        torneo = random.sample(individuos_lista, 2)
        
        # Mostrar los individuos seleccionados y sus fitness
        individuo_1, fitness_1 = torneo[0]
        individuo_2, fitness_2 = torneo[1]
        print(f"Torneo {i+1}:")
        print(f"  Indiv. {individuo_1} (fitness: {fitness_1}) vs Indiv. {individuo_2} (fitness: {fitness_2})")

        # Determinar el ganador del torneo
        if fitness_1 > fitness_2:
            ganador = individuo_1
            print(f"  Ganador: {individuo_1}\n")
        else:
            ganador = individuo_2
            print(f"  Ganador: {individuo_2}\n")
        
        # Guardar el ganador del torneo
        ganadores.append(ganador)

    return ganadores

# Llamada a la función para simular los torneos
ganadores = seleccion_por_torneo(individuos)

# Imprimir los ganadores de los torneos
print("Ganadores de los torneos:", ganadores)
