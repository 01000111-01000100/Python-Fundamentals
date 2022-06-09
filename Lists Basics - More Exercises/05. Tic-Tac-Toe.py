first_row = input().split()
second_row = input().split()
third_row = input().split()

first_player_wins = first_row == ["1", "1", "1"] or second_row == ["1", "1", "1"] or third_row == ["1", "1", "1"]
second_player_wins = first_row == ["2", "2", "2"] or second_row == ["2", "2", "2"] or third_row == ["2", "2", "2"]

for i1, r1 in enumerate(first_row):
    for i2, r2 in enumerate(second_row):
        for i3, r3 in enumerate(third_row):
            if (i1 == 0 and i2 == 0 and i3 == 0) or \
                    (i1 == 1 and i2 == 1 and i3 == 1) or \
                    (i1 == 2 and i2 == 2 and i3 == 2) or \
                    (i1 == 0 and i2 == 1 and i3 == 2) or \
                    (i1 == 2 and i2 == 1 and i3 == 0):
                if r1 == "1" and r2 == "1" and r3 == "1":
                    first_player_wins = True
                    break
                elif r1 == "2" and r2 == "2" and r3 == "2":
                    second_player_wins = True
                    break
if first_player_wins:
    print("First player won")
elif second_player_wins:
    print("Second player won")
else:
    print("Draw!")