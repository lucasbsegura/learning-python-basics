class NumberHolder:
    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number

obj = NumberHolder(7)
print(obj.returnNumber())