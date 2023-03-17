from cart import Cart
from product import Product
if __name__ == "__main__":
    cart = Cart()
    apple = Product("apple", 0.5)
    water = Product("water", 2)
    bread = Product("bread", 6)
    orange = Product("orange", 2)
    cart.products.append(apple)
    for Product in cart.products:
        print(Product.name, Product.price)


