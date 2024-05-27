def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

num_points = int(input("Kaç nokta girmek istiyorsunuz? "))

points = []
for _ in range(num_points):
    x = float(input("X koordinatını girin: "))
    y = float(input("Y koordinatını girin: "))
    points.append((x, y))


distances = []


for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


min_distance = distances[0]
for d in distances:
    if d < min_distance:
        min_distance = d


print(f"Minimum mesafe: {min_distance}")
