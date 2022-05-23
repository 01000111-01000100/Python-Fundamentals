key = int(input())
number_of_lines = int(input())

message = ''
for num in range(number_of_lines):
    line = ord(input())
    message += chr(line + key)

print(message)
