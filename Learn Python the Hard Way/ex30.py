people = 30
cars = 40
buses = 15


if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

if buses > cars:
	print("That's too many buses.")
elif buses < cars:
	print("Maybe we could take the buses.")
else: 
	print("We still can't decide.")

if people > buses:
	print("Alright, let's just take the buses.")
else:
	print("Fine, let's stay home then.")

# The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of 
# the conditions evaluates to TRUE.

# Similar to the else, the elif statement is optional. However, unlike else, for which there can be at most one statement, 
# there can be an arbitrary number of elif statements following an if.