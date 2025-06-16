import random
import numpy as np
import pandas as pd

df = pd.read_csv('notas_1u.csv')
alumnos = df['Alumno'].tolist()
notas = df['Nota'].tolist()

def crear_cromosoma():
    cromosoma = []
    for i in range(39):
        examen = random.randint(0, 2)
        genes = [0, 0, 0]
        genes[examen] = 1
        cromosoma.extend(genes)
    return cromosoma

def decodificar_cromosoma(cromosoma):
    asignaciones = {'A': [], 'B': [], 'C': []}
    examenes = ['A', 'B', 'C']
    
    for i in range(39):
        idx = i * 3
        for j in range(3):
            if cromosoma[idx + j] == 1:
                asignaciones[examenes[j]].append(i)
                break
    
    return asignaciones

def calcular_fitness(cromosoma):
    asignaciones = decodificar_cromosoma(cromosoma)
    
    if any(len(asignaciones[ex]) != 13 for ex in ['A', 'B', 'C']):
        return -1000
    
    promedios = {}
    varianzas = []
    diversidades = []

    for examen in ['A', 'B', 'C']:
        indices = asignaciones[examen]
        notas_examen = [notas[i] for i in indices]

        promedios[examen] = np.mean(notas_examen)
        varianza = np.var(notas_examen)
        max_nota = max(notas_examen)
        min_nota = min(notas_examen)
        rango = max_nota - min_nota
        
        promedios[examen] = promedio
        varianzas.append(varianza)
        diversidades.append(rango)


    desviacion = np.std(list(promedios.values()))
    varianza_prom = np.mean(varianzas)
    diversidad_prom = np.mean(diversidades)

    fitness = -desviacion - 0.1 * varianza_prom + 0.05 *diversidad_prom
    return fitness

def mutacion(cromosoma):
    cromosoma_mutado = cromosoma.copy()
    
    alumno1 = random.randint(0, 38)
    alumno2 = random.randint(0, 38)
    
    idx1 = alumno1 * 3
    idx2 = alumno2 * 3
    
    examen1 = [i for i in range(3) if cromosoma_mutado[idx1 + i] == 1][0]
    examen2 = [i for i in range(3) if cromosoma_mutado[idx2 + i] == 1][0]
    
    if examen1 != examen2:
        cromosoma_mutado[idx1:idx1+3] = [0, 0, 0]
        cromosoma_mutado[idx1 + examen2] = 1
        
        cromosoma_mutado[idx2:idx2+3] = [0, 0, 0]
        cromosoma_mutado[idx2 + examen1] = 1
    
    return cromosoma_mutado

def algoritmo_genetico(generaciones=100, tam_poblacion=50):
    poblacion = [crear_cromosoma() for _ in range(tam_poblacion)]
    
    for gen in range(generaciones):
        fitness_scores = [(crom, calcular_fitness(crom)) for crom in poblacion]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)
        
        nueva_poblacion = []
        
        elite = int(tam_poblacion * 0.2)
        for i in range(elite):
            nueva_poblacion.append(fitness_scores[i][0])
        
        while len(nueva_poblacion) < tam_poblacion:
            padre = random.choice(poblacion[:tam_poblacion//2])
            hijo = mutacion(padre)
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion
        
        if gen % 20 == 0:
            mejor_fitness = fitness_scores[0][1]
            print(f"Generación {gen}: Mejor fitness = {mejor_fitness:.4f}")
    
    mejor_cromosoma = fitness_scores[0][0]
    return mejor_cromosoma

print("REPRESENTACIÓN BINARIA")
print("Problema: Distribuir 39 alumnos en 3 exámenes (A, B, C) de forma equitativa")
print("Cromosoma: 117 bits (39 alumnos × 3 bits cada uno)")
print("Gen: [0,1,0] significa alumno asignado a examen B\n")

mejor_solucion = algoritmo_genetico()
asignaciones_finales = decodificar_cromosoma(mejor_solucion)

print("\nDistribución final:")
for examen in ['A', 'B', 'C']:
    indices = asignaciones_finales[examen]
    notas_examen = [notas[i] for i in indices]
    promedio = np.mean(notas_examen)
    print(f"Examen {examen}: {len(indices)} alumnos, promedio = {promedio:.2f}")
    print(f"  Alumnos: {[alumnos[i] for i in indices[:5]]}... (mostrando primeros 5)")

print("\nVerificación de equilibrio:")
promedios = []
for examen in ['A', 'B', 'C']:
    indices = asignaciones_finales[examen]
    notas_examen = [notas[i] for i in indices]
    promedios.append(np.mean(notas_examen))
print(f"Desviación estándar entre promedios: {np.std(promedios):.4f}")