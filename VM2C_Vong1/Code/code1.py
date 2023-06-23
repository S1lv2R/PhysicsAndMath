from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

polygon = Polygon([(0,0), (450, 0), (450, 150), (150, 150), (300, 600), (0, 450)]) # Manh dat 3
#polygon = Polygon([(0,0), (100, 0), (100, 50), (0, 50)]) # Manh dat 1

S = 9
data = []
def convert(x): return (S/2) + S*x
for i in range(67):
    for j in range(50):
        point = Point(convert(j), convert(i))
        if polygon.contains(point):
        	data.append((convert(j), convert(i)))
        	
print(data)
