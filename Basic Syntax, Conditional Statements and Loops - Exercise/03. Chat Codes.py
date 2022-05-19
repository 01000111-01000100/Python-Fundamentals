number = int(input())

for i in range(number):
    code_number = int(input())
    if code_number == 88:
        print("Hello")
    elif code_number == 86:
        print("How are you?")
    elif code_number != 88 and code_number != 86 and code_number < 88:
        print("GREAT!")
    elif code_number > 88:
        print("Bye.")
