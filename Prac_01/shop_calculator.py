number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for count in range(number_of_items):
    cost = float(input("Price of item: "))
    total_price += cost
if total_price > 100:
    discount = total_price * .10
    total_price -= discount
print("Total price for", number_of_items, "items is", "${:.2f}".format(total_price))
