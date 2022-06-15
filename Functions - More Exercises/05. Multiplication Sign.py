def multiplication_sign(num_list):
    negs = 0
    if "0" in num_list:
        return "zero"
    for elem in num_list:
        if "-" in elem:
            negs += 1
    if negs % 2 == 0:
        return "positive"
    else:
        return "negative"


num_list = [input(), input(), input()]
print(multiplication_sign(num_list))