class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

my_obj = MyClass()
print(my_obj.variable)

my_obj2 = MyClass()
my_obj2.variable = "lala"
print(my_obj2.variable)

my_obj.function()
