import numpy as np

x = np.array([185, 170, 168, 179, 182, 188])
y = np.array([72, 56, 60, 68, 72, 77])

k = 2

def coseno_distancia(point1, point2):
    dot_product = np.dot(point1, point2)
    norm_point1 = np.linalg.norm(point1)
    norm_point2 = np.linalg.norm(point2)
    return 1 - (dot_product / (norm_point1 * norm_point2))

np.random.seed(0)
centroid_indices = np.random.choice(range(len(x)), k, replace=False)
centroids = list(zip(x[centroid_indices], y[centroid_indices]))

max_iterations = 100
for iteration in range(max_iterations):
    # Inicializar clusters vacíos
    clusters = [[] for _ in range(k)]

    for i in range(len(x)):
        point = (x[i], y[i])
        distances = [coseno_distancia(point, centroid) for centroid in centroids]
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
