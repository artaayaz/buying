# our inventory
products = {
    "1": {
        "name": "shoe",
        "price": 40,
        "amount": 10
    },

    "2": {
        "name": "purse",
        "price": 60,
        "amount": 5
    },

    "3": {
        "name": "perfume",
        "price": 100,
        "amount": 8
    },
    "4": {
        "name": "hat",
        "price": 30,
        "amount": 3
    }
}


# greeting message
print("welcome to our store :)")
# showing inventory for customer
print("", products["1"], "\n",products["2"], "\n",products["3"], "\n",products["4"], "\n")
total_cost = 0
total_item = 0
# getting the id of items and purchasing them
while True:
    shop = int((input("write the id you want :")))
    if shop == 1:
        quantity = int(input("enter qnty:"))
        cost = products["1"]["price"] * quantity
        print(f"you purchased {quantity} per of shoe")
        print(f"cost:{cost} $")
        products["1"]["amount"] -= quantity
        total_cost += cost
        total_item += quantity

    elif shop == 2:
        quantity = int(input("enter qnty:"))
        cost = products["2"]["price"] * quantity
        print(f"you purchased {quantity} purse")
        print(f"cost:{cost} $")
        products["2"]["amount"] -= quantity
        total_cost += cost
        total_item += quantity

    elif shop == 3:
        quantity = int(input("enter qnty:"))
        cost = products["3"]["price"] * quantity
        print(f"you purchased {quantity} perfume")
        print(f"cost:{cost} $")
        products["3"]["amount"] -= quantity
        total_cost += cost
        total_item += quantity

    elif shop == 4:
        quantity = int(input("enter qnty:"))
        cost = products["4"]["price"] * quantity
        print(f"you purchased {quantity} hats")
        print(f"cost:{cost} $")
        products["4"]["amount"] -= quantity
        total_cost += cost
        total_item += quantity

    elif shop == 0:
        print("shopping is done!")
        break

    else:
        print("we dont have that id!!try again!")
# customer's shopping cart
print(f"you purchased {total_item} items.")
print("your total cost is: ", total_cost, "$")
# inventory
print("", products["1"], "\n",products["2"], "\n",products["3"], "\n",products["4"], "\n")

