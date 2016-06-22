my_name = 'Edward'
my_age = 28
my_height = 66 # inches
my_weight = 177
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He weighs %d pounds." % my_weight)
print ("Actually that is not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d, I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight))