def min_number(number):
    return min(number)

def max_number(number):
    return max(number)

def sum_of_number(number):
    return sum(number)

num = [int(a) for a in input().split(' ')]

print(f"The minimum number is {min_number(num)}")
print(f"The maximum number is {max_number(num)}")
print(f"The sum number is: {sum_of_number(num)}")
