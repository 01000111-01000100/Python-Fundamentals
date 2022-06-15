single_number = input()

sum_of_odd_digits = 0
sum_of_even_digits = 0

for sub in single_number:
    for ele in str(sub):

        if int(ele) % 2 == 0:
            sum_of_even_digits += int(ele)
        else:
            sum_of_odd_digits += int(ele)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")