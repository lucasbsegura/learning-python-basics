my_pets = ['alfred', 'thabita', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))
print(result)

result2 = list(map(round, circle_areas, range(1, 3)))
print(result2)

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(zip(my_strings, my_numbers))
print(results)

my_strings2 = ['a', 'b', 'c', 'd', 'e']
my_numbers2 = [1, 2, 3, 4, 5]
results = list(map(lambda x, y: (x, y), my_strings2, my_numbers2))
print(results)

