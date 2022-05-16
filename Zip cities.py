x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
cities = ["MARRAKECH", "LONDON", "PARIS", "NEW YORK", "MOSCOW", "DUBAI", "TOKYO", "SINGAPORE"]

points = []
# here our for loop 
for point in zip(cities, x_coord, y_coord, z_coord):
    points.append("{} : {}, {}, {}".format(*point))

for point in points:
    print(point)