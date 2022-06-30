number_of_electrons = int(input())
list_of_shells = []
index = 0

while 0 < number_of_electrons:

    index += 1
    shell = 2 * index ** 2

    if number_of_electrons >= shell:
        list_of_shells.append(shell)
        number_of_electrons -= shell
    else:
        list_of_shells.append(number_of_electrons)
        number_of_electrons = 0

print(list_of_shells)