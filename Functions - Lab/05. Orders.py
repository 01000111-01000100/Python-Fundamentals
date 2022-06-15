def order(product, number):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1.00
    elif product == "snacks":
        price = 2.00
    return price * number


new_product = input()
quantity = int(input())

print(f"{order(new_product, quantity):.2f}")