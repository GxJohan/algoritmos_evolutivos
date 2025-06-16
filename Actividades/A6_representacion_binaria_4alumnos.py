import random
import numpy as np
import pandas as pd

df = pd.read_csv('notas_1u.csv')
alumnos = df['Alumno'].tolist()
notas = df['Nota'].tolist()

def crear_cromosoma():
    cromosoma = []
    for _ in range(39):
        gen = [0, 0, 0, 0]
        gen[random.randint(0, 3)] = 1
        cromosoma.extend(gen)
    return cromosoma

def decodificar_cromosoma(cromosoma):
    asignaciones = {'A': [], 'B': [], 'C': [], 'D': []}
    examenes = ['A', 'B', 'C', 'D']
    
    for i in range(39):
        idx = i * 4
        for j in range(4):
            if cromosoma[idx + j] == 1:
                asignaciones[examenes[j]].append(i)
                break
    return asignaciones

def calcular_fitness(cromosoma):
    asignaciones = decodificar_cromosoma(cromosoma)
    
    if any(len(asignaciones[ex]) not in [9, 10] for ex in ['A', 'B', 'C', 'D']):
        return -1000

    promedios = []
    for examen in ['A', 'B', 'C', 'D']:
        notas_examen = [notas[i] for i in asignaciones[examen]]
        promedios.append(np.mean(notas_examen))

    return -np.std(promedios)

def mutacion(cromosoma):
    cromosoma_mutado = cromosoma.copy()
    
    alumno1 = random.randint(0, 38)
    alumno2 = random.randint(0, 38)
    
    idx1 = alumno1 * 4
    idx2 = alumno2 * 4
    
    examen1 = [i for i in range(4) if cromosoma_mutado[idx1 + i] == 1][0]
    examen2 = [i for i in range(4) if cromosoma_mutado[idx2 + i] == 1][0]
    
    if examen1 != examen2:
        cromosoma_mutado[idx1:idx1+4] = [0, 0, 0, 0]
        cromosoma_mutado[idx1 + examen2] = 1
        
        cromosoma_mutado[idx2:idx2+4] = [0, 0, 0, 0]
        cromosoma_mutado[idx2 + examen1] = 1
    
    return cromosoma_mutado

def algoritmo_genetico(generaciones=150, tam_poblacion=60):
    poblacion = [crear_cromosoma() for _ in range(tam_poblacion)]
    
    for gen in range(generaciones):
        fitness_scores = [(crom, calcular_fitness(crom)) for crom in poblacion]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)
        
        nueva_poblacion = []
        
        elite = int(tam_poblacion * 0.2)
        for i in range(elite):
            nueva_poblacion.append(fitness_scores[i][0])
        
        while len(nueva_poblacion) < tam_poblacion:
            padre = random.choice(poblacion[:tam_poblacion // 2])
            hijo = mutacion(padre)
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion
        
        if gen % 30 == 0:
            print(f"Generación {gen}: Mejor fitness = {fitness_scores[0][1]:.4f}")
    
    return fitness_scores[0][0]

# MAIN
print("REPRESENTACIÓN BINARIA CON 4 EXÁMENES")
print("Distribuir 39 alumnos en A, B, C y D de forma equilibrada\n")

mejor_solucion = algoritmo_genetico()
asignaciones_finales = decodificar_cromosoma(mejor_solucion)

print("\nDistribución final:")
for examen in ['A', 'B', 'C', 'D']:
    indices = asignaciones_finales[examen]
    notas_examen = [notas[i] for i in indices]
    promedio = np.mean(notas_examen)
    print(f"Examen {examen}: {len(indices)} alumnos, promedio = {promedio:.2f}")
    print(f"  Alumnos: {[alumnos[i] for i in indices[:5]]}...")

print("\nVerificación de equilibrio:")
promedios = []
for examen in ['A', 'B', 'C', 'D']:
    indices = asignaciones_finales[examen]
    notas_examen = [notas[i] for i in indices]
    promedios.append(np.mean(notas_examen))
print(f"Desviación estándar entre promedios: {np.std(promedios):.4f}")
