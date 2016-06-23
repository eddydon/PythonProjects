age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

# Why would I use %r over %s?
# Remember, %r is for debugging and is “raw representation” while %s is for display.
print(("So, you're %r old, %r tall and %r lbs heavy.") % (age, height, weight))