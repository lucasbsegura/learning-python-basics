def sum(a, b):
    return a + b

a, b = 1, 2
c = sum(a, b)
print(c)

#--- with lambda
sum_lambda = lambda x, y : x + y
l = sum_lambda(a, b)
print(c)