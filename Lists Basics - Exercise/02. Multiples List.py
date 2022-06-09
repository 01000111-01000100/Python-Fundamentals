first_number = int(input())
second_number = int(input())
sum_of_numbers = []
for multiplier in range(1, second_number + 1):
    sum_of_numbers.append(first_number * multiplier)
print(sum_of_numbers)