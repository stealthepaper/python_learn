class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def __calculate_average(self):
        total = sum(self.numbers)
        return total / len(self.numbers)


average_calculator = AverageCalculator([1, 2, 3])
# print(dir(average_calculator))
# print(average_calculator.__calculate_average())
print(average_calculator._AverageCalculator__calculate_average())