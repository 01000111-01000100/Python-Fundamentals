population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

for i in range(len(population)):
    if population[i] < minimum_wealth:
        other_string = minimum_wealth - population[i]
        max_number = max(population)
        if max_number - other_string >= minimum_wealth:
            population[population.index(max_number)] -= other_string
            population[i] += other_string
if sum(population) >= len(population) * minimum_wealth:
    print(population)
else:
    print("No equal distribution possible")
