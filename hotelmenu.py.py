#creating Menu for Restaurant
menu = {
    'pizza':80,
    'berger':40,
    'Coffee':50,
    'Spring Roll':60,
    'Salad':70,
}
""" print(menu) """

payment = {
    'UPI':88168471,
}
""" print(payment) """

#Greetings to the Customer
print("WELCOME TO OUR RESTAURANT")
print("Pizza: 80/-\nBerger: 40/-\nCoffee: 50/-\nSpring Roll: 60/-\nSalad: 70/-")

Order_total = 0

Item_1 = input("Enter The Item You wish to Order =")
if Item_1 in menu:
    Order_total += menu[Item_1] #eg: 0+50(if you order coffee(as per your choice))
    print(f"Your Delicious {Item_1} has been added to your Order")

else:
    print(f"Oh Sorry :( {Item_1} is not Available yet!")


another_order = input("Do You Want to add Another item? (Yes/No)")
if another_order == "yes":
    item_2 = input("Enter The Name Of the Another Item = ")
    if item_2 in menu:
        Order_total += menu[item_2]
        print(f"{item_2} has been added to Cart")
    
    else:
        print(f"Ordered Item {item_2} is not available Sorry!")

print(f"The Total amount of items to pay is {Order_total}")
print("You Can Pay Through UPI/CREDIT CARD/DEBIT CARD\n Sorry Currently Our Restaurant is Accepting UPI Payments and Cash Only")
print(payment)
