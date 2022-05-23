party_size = int(input())
days = int(input())

coins = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        party_size -= 2

    if day % 3 == 0 and day % 5 == 0:
        party_size += 5

    coins += 50 - (party_size * 2)

    if day % 3 == 0:
        coins -= party_size * 3

    if day % 5 == 0:
        coins += party_size * 20

        if day % 3 == 0:
            coins -= party_size * 2

total_coins = int((coins / party_size))

print(f"{party_size} companions received {total_coins} coins each.")