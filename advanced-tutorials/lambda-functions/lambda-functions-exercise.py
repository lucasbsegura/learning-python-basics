#Write a program using lambda functions to check if a number in the given list 
# is odd. Print "True" if the number is odd or "False" if not for each element.

is_odd = lambda a : (a % 2) == 1

l = [2,4,7,3,14,19]
for i in l:
    print(is_odd(i))