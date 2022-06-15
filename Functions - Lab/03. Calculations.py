import operator

def calculation(number_a, number_b, operation):
    operations_dict = {'multiply': operator.mul, 'divide': operator.truediv,
                       'add': operator.add, 'subtract': operator.sub}
    return int(operations_dict[operation](number_a, number_b))

type_of_operation = input()
first_number = int(input())
second_number = int(input())
print(calculation(first_number, second_number, type_of_operation))