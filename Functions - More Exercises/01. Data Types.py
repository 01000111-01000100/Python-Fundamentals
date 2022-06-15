def data_type(funk,num):
    if funk == "int":
        return int(num) * (2)
    elif funk == "real":
        return f"{(float(num) * 1.5):.2f}"
    elif funk == "string":
        return f"${num}$"


new_function = input()
number = input()

print(data_type(new_function, number))