name = "John"
print("Hello, %s" % name)

#to use two or more argument specifiers, use a tuple (parentheses):
hello = "Hello"
print("%s, %s" % (hello, name))

age = 23
print("%s is %d years old" % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

#some basic argument specifiers you should know:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of 
#  digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)