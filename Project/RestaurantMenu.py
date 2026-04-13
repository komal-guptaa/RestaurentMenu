menu = {
    'pizza':100,
    'Pasta': 80,
    'Burger':50,
    'Coffee':70,
    'Cold Drink':40,
}
print("Welocome TO Our Restaurant")
print("pizza:100\nPasta: 80\nBurger:50\nCoffee:70\nCold Drink:40")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order ")
else:
    print(f"Ordered item {item_1} is not avaialable yet!")
    
another_order = input("Do you want to add another item?(yes / No)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2 }has been added to your order")
    else:
        print(f"item {item_2}is not avaliable")


print(f"The total amount of items to pay is {order_total}")

if order_total > 0:
    print(f"Total amount to pay = {order_total}")
    print("Enjoy your order 😊")
else:
    print("Enjoy your day 😊")