def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


num_points = int(input("How many points do you want to enter? "))

points = []
for i in range(num_points):
    coordinates = input(f"Enter the coordinates for point {i+1} (x,y) without parentheses: ")
    x, y = map(float, coordinates.split(','))
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


print(f"Minimum distance: {min_distance}")
