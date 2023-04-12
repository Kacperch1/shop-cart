from cart import Cart
from product import Product

apple = Product("apple", 0.5)
water = Product("water", 2)
bread = Product("bread", 6)
orange = Product("orange", 2)

if __name__ == "__main__":
    cart = Cart()
    cart.products.append(apple)
    cart.products.append(water)
    cart.products.append(orange)

    for Product in cart.products:
        print(Product.name, Product.price)

# TODO
# 1. Calculate the costs of all products in the chart -> There are few ways to doing it.  Prepare at least 2 alternative solutions

##option 1
total_cost = 0
for product in cart.products:
    total_cost += product.price
print("Total cost:", total_cost)

##option 2
total_cost = sum([product.price for product in cart.products])
print("Total cost:", total_cost)