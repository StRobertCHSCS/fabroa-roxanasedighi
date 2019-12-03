# initialize the total
total = 0

# get the products and quantity and add them to the total
for i in range(1, 4):
    price = float(input("Enter the price of the product " + str(i) + ": "))
    qty = int(input("Enter the quantity of the product " + str(i) + ": "))

    total = total + (price * qty)

total =+ total * 0.13
print(round(total,2))
