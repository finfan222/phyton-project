class Num:
    number = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return "My number: " + str(self.number)

    def min(self, right):
        return self.number if self.number <= right else right

    def max(self, right):
        return self.number if self.number >= right else right

    def between(self, left, right):
        return True if left <= self.number <= right else False
