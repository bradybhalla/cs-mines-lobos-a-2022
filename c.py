import math

def angle_diff(a1, a2, diff):
	p1 = [math.cos(a1), math.sin(a1)]
	p21 = [math.cos(a2+diff), math.sin(a2+diff)]
	p22 = [math.cos(a2-diff), math.sin(a2-diff)]
	if abs(p1[0]-p21[0]) < 0.01 and abs(p1[1]-p21[1]) < 0.01:
		return True
	return abs(p1[0]-p22[0]) < 0.01 and abs(p1[1]-p22[1]) < 0.01

class Side:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.mag = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
		self.angle = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
		if self.angle < 0:
			self.angle += 2*math.pi

points = [[int(i) for i in input().split(" ")] for j in range(4)]

average = (sum(i[0] for i in points)/4, sum(i[1] for i in points)/4)
points_order = sorted(points, key=lambda p: math.atan2(p[1]-average[1], p[0]-average[0]))

sides = []
for i in range(4):
	sides.append(Side(points_order[i], points_order[(i+1)%4]))

c = "Quadrilateral"
if sides[0].mag==sides[1].mag and sides[2].mag == sides[3].mag:
	c = "Kite"
elif sides[1].mag==sides[2].mag and sides[3].mag == sides[0].mag:
	c = "Kite"

if angle_diff(sides[0].angle, sides[2].angle, math.pi):
	c = "Trapezoid"
elif angle_diff(sides[1].angle, sides[3].angle, math.pi):
	c = "Trapezoid"

if angle_diff(sides[0].angle, sides[2].angle, math.pi) and angle_diff(sides[1].angle, sides[3].angle, math.pi):
	c = "Parallelogram"

if c=="Parallelogram":
	if all(i.mag == sides[0].mag for i in sides):
		c = "Rhombus"
	if angle_diff(sides[0].angle, sides[1].angle, math.pi/2):
		if angle_diff(sides[1].angle, sides[2].angle, math.pi/2):
			c = "Rectangle"

if c=="Rectangle":
	if all(i.mag == sides[0].mag for i in sides):
		c = "Square"

print(c)


