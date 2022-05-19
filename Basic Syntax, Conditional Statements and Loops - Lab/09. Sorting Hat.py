names = input()

while names != "Welcome!" and names != "Voldemort":
    nameInNumbers = len(names)
    if nameInNumbers < 5:
        print(f"{names} goes to Gryffindor.")
    elif nameInNumbers == 5:
        print(f"{names} goes to Slytherin.")
    elif nameInNumbers == 6:
        print(f"{names} goes to Ravenclaw.")
    elif nameInNumbers > 6:
        print(f"{names} goes to Hufflepuff.")
    names = input()

    while names == "Voldemort":
        print("You must not speak of that name!")
        break

if names != "Voldemort":
    print("Welcome to Hogwarts.")
