x = 2
print(x == 2)
print(x == 3)
print(x < 3)

# BOOLEAN operator
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# IN operator
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    print("Statement is True.")
    pass
elif another_statement is True:
    print("Another statement is True.")
    pass
else: 
    print("Something else.")
    pass

if x == 2:
    print("x equals two.")
else:
    print("x does not equal to two.")

# IS operator
y = [1,2,3]
z = [1,2,3]
print(y == z)
print(y is z)

# NOT operator
print(not False)
print((not False) == (False))