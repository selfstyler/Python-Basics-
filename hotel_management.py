#define the menu of resturant
menu = {
    'pizza':40, 
    'pasta':30, 
    'salad':10,
    'coffee':50,
}

#greet
print("Welcome to the adv py hotel")
print("pizza: rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs10\nCoffee: Rs50")

order_total = 0
#80 + 70 = 150 

item_1 = input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f"Your item {item_1} has been added")
    
else:
    print(f"your item {item_1} is not available ")
    
another_order = input("Do you want to add another order? ")

if another_order == "Yes":
    
    item = input("enter the name of second item = ")
    
    
    
    if item in menu:
            
    
        order_total += menu[item]
        print(f"Orderd {item} has been added ")
    else:
        print(f"{item} is not available ")
    
    
print(f"THe total amount of items to pay is {order_total}") 
    