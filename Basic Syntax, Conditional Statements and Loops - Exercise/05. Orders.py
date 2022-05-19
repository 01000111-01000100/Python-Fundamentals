orders = int(input())

total_price = 0

for order in range(0, orders, 1):
    price = float(input())
    days = int(input())
    capsule = int(input())
    if (price >= 0.01 and price <= 100) and (days >= 1 and days <= 31) and (capsule >= 1 and capsule <= 2000):
        price_day = price * days * capsule
        if price_day != 0:
            print(f"The price for the coffee is: ${price_day:.2f}")
        total_price += price_day

print(f"Total: ${total_price:.2f}")