n = int(input())

ships = []
for i in range(1, n + 1):
    field = [list(map(int, input().split()))]
    ships += field

attacked = input().split(" ")

destroyed = 0
for shot in range(len(attacked)):
    current_attack = attacked[shot]
    row = int(current_attack[0])
    col = int(current_attack[2])
    ships[row][col] -= 1

    if ships[row][col] == 0:
        destroyed += 1

print(destroyed)