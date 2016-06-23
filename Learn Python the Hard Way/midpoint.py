def midpoint(pt1, pt2):
	x1, y1 = pt1 # Extract x and y components from the first point
	x2, y2 = pt2 # Extract x and y components from the second point
	return (x1 + x2) / 2 , (y1 + y2) / 2

# Get two points from the user
point1 = eval(input("Enter first point (x, y): "))
point2 = eval(input("Enter second point (x, y): "))

# Compute the midpoint
mid = midpoint(point1, point2)
# Report result to user
print("Midpoint of", point1, "and", point2, "is", mid)