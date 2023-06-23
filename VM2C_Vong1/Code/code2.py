import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

visited = []

"""
Manh dat 2:
k = 50*math.sqrt(3) - 75
polygon = Polygon([(0,0), (375 + k, 0), (225 + k, 150), (75 + k, 150)])
"""

"""
Manh dat 1:
polygon = Polygon([(0,0), (100, 0), (100, 50), (0, 50)])
"""

polygon = Polygon([(0,0), (450, 0), (450, 150), (150, 150), (300, 600), (0, 450)])

# Code [2]
def distance(p1, p2): return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def find_nearest_point(target):
	min_distance = float("inf")
	point = None
	for i in range(len(data)):
		distance_to_target = distance(data[i], target)
		if distance_to_target < min_distance and data[i] not in visited:
			min_distance = distance_to_target
			point = data[i]
	return point
	
def find_neighbors(start, max_points):
	points = [start]
	while len(points) < max_points:
		print(points)
		for p in points:
			neighbors = []
			for dx in [-9, 0, 9]:
				for dy in [-9, 0, 9]:
					if dx == dy == 0:
						continue
					neighbor = (p[0] + dx, p[1] + dy)
					point = Point(p[0] + dx, p[1] + dy)
					if neighbor not in points and neighbor not in visited and polygon.contains(point):
						neighbors.append(neighbor)
			if len(points) + len(neighbors) > max_points:
				break
			points.extend(neighbors)
	visited.extend(points)
	return points

nearest_point = find_nearest_point((175 + k, 0))
print(nearest_point)
points = find_neighbors(nearest_point, 149)
print(points)
