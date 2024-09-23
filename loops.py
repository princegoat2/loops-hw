muffins = 10
cupcakes = 10

while muffins > 0 or cupcakes > 0:
   
    choice = input("would you like a muffin, a cupcake, or type '0' to end the sale? ").lower()
   
    if choice == "0":
        break
   
    elif choice == "muffin":
        if muffins > 0:
            muffins -= 1
            print(f"muffins: {muffins} cupcakes: {cupcakes}")
        else:
            print("none left.")
   
    elif choice == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
            print(f"muffins: {muffins} cupcakes: {cupcakes}")
        else:
            print("none left")
   
    else:
        print("type 'muffin', 'cupcake', or '0' to end the sale.")

print(f"muffins: {muffins} cupcakes: {cupcakes}")
