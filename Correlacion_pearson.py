import numpy as np

# Datos de entrada
x = np.array([185, 170, 168, 179, 182, 188])
y = np.array([72, 56, 60, 68, 72, 77])

# Función para calcular el coeficiente de correlación de Pearson
def pearson_correlacion(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    x_deviation = x - mean_x
    y_deviation = y - mean_y
    numerator = np.sum(x_deviation * y_deviation)
    denominator = np.sqrt(np.sum(x_deviation**2) * np.sum(y_deviation**2))
    correlation = numerator / denominator
    return correlation

correlacion = pearson_correlacion(x, y)

print(f"Coeficiente de Correlación de Pearson: {correlacion}")
