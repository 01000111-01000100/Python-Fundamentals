text = input()
no_print = False
while not text == "End":
    if text == "SoftUni":
        no_print = True
    if not no_print:
        for letter in range(len(text)):
            print(text[letter] * 2, end='')
        print()
    no_print = False
    text = input()