products = [
    {
        "id": 1,
        "name": "shoe",
        "price": 40,
        "amount": 10
    },
    {
        "id": 2,
        "name": "purse",
        "price": 60,
        "amount": 5
    },
    {
        "id": 3,
        "name": "perfume",
        "price": 100,
        "amount": 8
    },
    {
        "id": 4,
        "name": "hat",
        "price": 30,
        "amount": 3
    }
]
print("welcome to our store :)")
print(products)

total_cost = 0
total_item = 0
while True:
    item = int((input("write the id you want :")))
    if item == 0:
        print("total items: {}".format(total_item))
        print("total cost: {}".format(total_cost))
        break
    quantity = int(input("enter qnty:"))
    product = None
    for p in products:
        if p.get("id") == item:
            product = p

    if not product:
        print("product id is wrong")
    
    if product.get("amount") < quantity:
        print("we don't have that much")
    
    cost = product.get("price") * quantity
    total_cost += cost
    total_item += quantity
    for p in products:
        if p.get("id") == item:
            p["amount"] -= quantity


