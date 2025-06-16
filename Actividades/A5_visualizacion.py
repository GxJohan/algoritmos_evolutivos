import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Leer notas y alumnos
df = pd.read_csv('notas_1u.csv')
alumnos = df['Alumno'].tolist()
notas = df['Nota'].tolist()

# 1. Evolución del fitness por generación (simulado)
fitness_evol_binaria = [-0.22, -0.1, -0.06, -0.04, -0.0363]
fitness_evol_real = [-1.1, -1.08, -1.07, -1.06, -1.05]
fitness_evol_permut = [0.03, 0.12, 0.19, 0.23, 0.2637]

generaciones = [0, 20, 40, 60, 80]

plt.figure(figsize=(10, 5))
plt.plot(generaciones, fitness_evol_binaria, label="Binaria")
plt.plot(generaciones, fitness_evol_real, label="Real")
plt.plot(generaciones, fitness_evol_permut, label="Permutacional")
plt.xlabel("Generaciones")
plt.ylabel("Mejor Fitness")
plt.title("Evolución del Fitness por Representación")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Histograma de notas por examen
asignaciones = {
    'A': [15, 14, 13, 16, 17, 11, 12, 18, 19, 14, 13, 16, 15],
    'B': [15, 16, 17, 19, 20, 13, 12, 11, 10, 13, 14, 17, 15],
    'C': [14, 13, 16, 17, 18, 15, 14, 11, 9, 10, 13, 12, 19]
}

plt.figure(figsize=(10, 5))
for examen, notas_examen in asignaciones.items():
    sns.histplot(notas_examen, kde=False, label=f'Examen {examen}', bins=6)

plt.xlabel("Notas")
plt.ylabel("Frecuencia")
plt.title("Distribución de Notas por Examen")
plt.legend()
plt.tight_layout()
plt.show()

# 3. Comparación de promedios por examen entre representaciones
examenes = ['Examen A', 'Examen B', 'Examen C']
promedios_binaria = [15.46, 15.38, 15.38]
promedios_real = [15.38, 15.46, 15.38]
promedios_permutacional = [15.38, 15.46, 15.38]

x = np.arange(len(examenes))  # Posiciones para Examen A, B, C
width = 0.25  # Ancho de las barras

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar barras para cada representación
bars1 = ax.bar(x - width, promedios_binaria, width, label='Binaria', color='orange')
bars2 = ax.bar(x, promedios_real, width, label='Real', color='orangered')
bars3 = ax.bar(x + width, promedios_permutacional, width, label='Permutacional', color='crimson')

# Título y etiquetas
ax.set_ylabel('Promedio de Notas')
ax.set_title('Comparación de Promedios por Representación')
ax.set_xticks(x)
ax.set_xticklabels(examenes)
ax.legend()

# Mostrar valores encima de cada barra
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # desplazamiento vertical
                    textcoords="offset points",
                    ha='center', va='bottom')

# Ajustes de escala
plt.ylim(15.2, 15.6)
plt.tight_layout()
plt.show()