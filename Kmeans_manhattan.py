import numpy as np

x = np.array([185, 170, 168, 179, 182, 188])
y = np.array([72, 56, 60, 68, 72, 77])

k = 2

def manhattan_distancia(point1, point2):
    return np.abs(point1[0] - point2[0]) + np.abs(point1[1] - point2[1])

np.random.seed(0)
centroides_x = [170, 56]
centroides_y = [188, 77]
centroids = list(zip(centroides_x, centroides_y))

max_iterations = 100
for iteration in range(max_iterations):
    # Inicializar clusters vacíos
    clusters = [[] for _ in range(k)]


    for i in range(len(x)):
        point = (x[i], y[i])
        distances = [manhattan_distancia(point, centroid) for centroid in centroids]
        cluster_index = np.argmin(distances)
        clusters[cluster_index].append(point)

    new_centroids = [np.mean(cluster, axis=0) for cluster in clusters]


    if np.array_equal(centroids, new_centroids):
        break
    centroids = new_centroids

for i in range(k):
    print(f'Cluster {i + 1}:')
    for point in clusters[i]:
        print(point)
