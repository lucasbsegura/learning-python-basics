#The target of this exercise is to create a string, an integer,
# and a floating point number. 
#The string should be named mystring and should contain the word "hello". 
#The floating point number should be named myfloat and should 
# contain the number 10.0, and the integer should be named myint and 
# should contain the number 20.

mystring = "hello"
myfloat = float(10)
myint = 20

#testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Int: %d" % myint)
