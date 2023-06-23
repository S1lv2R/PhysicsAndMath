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

# Manh dat 3:
polygon = Polygon([(0,0), (450, 0), (450, 150), (150, 150), (300, 600), (0, 450)])

def find_neighbors(start, max_points):
	points = [start]
	while len(points) < max_points:
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

