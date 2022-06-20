def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))

multiplywith4 = multiplier_of(4)
print(multiplywith4(9))