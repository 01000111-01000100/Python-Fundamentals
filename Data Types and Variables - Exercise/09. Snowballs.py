number_of_snowballs = int(input())
best_snowball_qiality = 0
best_snowball_data = ''

for _ in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight / time) ** quality

    if result > best_snowball_qiality:
        best_snowball_qiality = result
        best_snowball_data = f'{weight} : {time} = {int(result)} ({quality})'

print(best_snowball_data)