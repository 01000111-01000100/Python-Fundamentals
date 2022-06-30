seq_of_numbers = list(map(int, input().split(", ")))
list_of_numbers = []
group = 0
while len(seq_of_numbers) > 0:
    group += 1
    for number in seq_of_numbers:
        if int(number) <= group * 10:
            list_of_numbers.append(number)
    print(f"Group of {group}0's: {list_of_numbers}")
    for copy in list_of_numbers:
        if copy in seq_of_numbers:
            seq_of_numbers.remove(copy)
    list_of_numbers.clear()