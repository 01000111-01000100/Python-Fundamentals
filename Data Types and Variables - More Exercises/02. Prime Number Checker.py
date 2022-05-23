import math

num = int(input())
is_prime = True
if num < 2:
    is_prime = False

else:
    for i in range(2, math.floor(math.sqrt(num))):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("True")
else:
    print("False")