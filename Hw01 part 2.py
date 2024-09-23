family_members = 4
pizza_slices = 8

slices_full_meal = int(input("How many slices each family recieves for full meal: "))

needed_pizzas_slices = slices_full_meal * family_members

pizzas_bought = (needed_pizzas_slices + pizza_slices - 1) // pizza_slices

leftovers = pizza_slices * pizzas_bought - needed_pizzas_slices

print(f'\nThe amount of pizzas needed to be bought is: {pizzas_bought}')

print(f'\nThe amount of leftover slices: {leftovers}')