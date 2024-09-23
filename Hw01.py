pizza_slices = 8

member_One_Full = int(input("how many slices family member one wants: "))

member_Two_Full = int(input("how many slices family member two wants: "))

member_Three_Full = int(input("how many slices family member three wants: "))

member_Four_Full = int(input("how many slices family member four wants: "))

needed_pizza_slices = member_One_Full + member_Two_Full + member_Three_Full + member_Four_Full 

pizzas_bought = (needed_pizza_slices + pizza_slices - 1) // pizza_slices

leftovers = pizza_slices * pizzas_bought - needed_pizza_slices

print(f'\nThe amount of pizzas needed to be bought is: {pizzas_bought}')

print(f'\nThe amount of leftover slices: {leftovers}')