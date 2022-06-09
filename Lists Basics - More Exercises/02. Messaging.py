numbers = input().split(" ")
message = input()
sum_list = []

for num in numbers:
    numbers_sum = 0
    for i in num:
        numbers_sum += int(i)
    sum_list.append(numbers_sum)

for index in range(len(sum_list)):
    letter_to_remove = ""
    result = sum_list[index] % len(message)
    letter_to_remove += message[result]
    print(letter_to_remove, end='')
    new_message = message.replace(str(letter_to_remove), "", 1)
    message = new_message