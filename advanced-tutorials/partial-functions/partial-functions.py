from audioop import mul
from functools import partial

#An important note: the default values will start replacing variables from the left. 
# The 2 will replace x. y will equal 4 when dbl(4) is called.
def multiply(x, y):
    return x * y

dbl = partial(multiply, 2)
print(dbl(4))

