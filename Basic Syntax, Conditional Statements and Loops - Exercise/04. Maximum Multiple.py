import sys

positive_number = int(input())
number = int(input())

max_number = -sys.maxsize
for i in range(0, number+1, positive_number):
    if i > max_number:
        max_number = i
print(max_number)