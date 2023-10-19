import numpy as np
import matplotlib.pyplot as plt


x = np.array([185, 170, 168, 179, 182, 188])
y = np.array([72, 56, 60, 68, 72, 77])

k = 2


def distancia_euclidiana(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

centroides_x = [185, 72]
centroides_y = [170, 56]
centroides = list(zip(centroides_x, centroides_y))

max_iterations = 100
for iteration in range(max_iterations):
    clusters = [[] for _ in range(k)]

    # Asignar puntos a clústeres
    for i in range(len(x)):
        point = (x[i], y[i])
        
        distances = [distancia_euclidiana(point, centroides) for centroides in centroides]
        cluster_index = np.argmin(distances)
        clusters[cluster_index].append(point)
        print("------------------------------------------------------------")
        #print("\n")
        print("Cluster: ", cluster_index, "Punto:  ", point, "\n")
    new_centroides = [np.mean(cluster, axis=0) for cluster in clusters]

    if np.array_equal(centroides, new_centroides):
        break
    centroides = new_centroides


for i in range(k):
    print(f'Cluster {i + 1}:')
    for point in clusters[i]:
        print(point)

#print("NUEVOS CENTROIDEEEEEES", new_centroides)
