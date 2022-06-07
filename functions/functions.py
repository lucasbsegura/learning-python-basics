def my_function():
    print("Hello from my Function!")
my_function()

def my_function_with_args(username, greeting):
    print("Hello, %s, from my Function! I wish you %s" % (username, greeting))
my_function_with_args(username="Lucas", greeting="a great day!!")

def sum_two_numbers(a, b):
    return a + b
sum = sum_two_numbers(1, 2)
print(sum)