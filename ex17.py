# We’re going to actually write a Python script to copy one file to another. 
# It’ll be very short but will give you some ideas about other things you can do with fi les.


from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line
in_file = open(from_file)
indata = in_file.read()

# What does the len() function do?
# It gets the length of the string that you pass to it and then returns that as a number. Play with it.
print(("The input file is %d bytes long") % len(indata))

print(("Does the output file exist? %r") % exists(to_file))
print("Ready , hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()