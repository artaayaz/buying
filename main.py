from buying.product import Product
from buying.errors import ProductNotFound

products = Product()

print(products.get_all())

total_cost = 0
total_item = 0
while True:
    item = int(input("write the id you want :"))
    if item == 0:
        break
    product = None
    try:
        product = products.get(item)
    except (ProductNotFound, ValueError) as e:
        print(e)
        continue

    quantity = int(input("enter qnty:"))

    if product.amount < quantity:
        print("we don't have that much")
    
    cost = product.price * quantity
    total_cost += cost
    total_item += quantity
    products.buy(item, quantity)
    print("cost: {}".format(cost))
    print("quantity: {}".format(quantity))

print("total quantity: {}".format(total_item))
print("total cost: {}".format(total_cost))