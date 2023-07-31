from cart import Cart
from product import Product

##creating fuction which add products to cart
def buy_products(cart, products):
    while True:
        product_name = input("What product do you need (type 'done' to finish shopping): ").lower()
        if product_name == "done":
            break

        if product_name in products:
            product = products[product_name]
            quantity = int(input(f"How many {product_name}s do you want? "))
            cart.products.extend([product] * quantity)
            print(f"Added {quantity} {product_name}(s) to your cart.")
        else:
            print(f"Sorry, we don't have {product_name} in stock.")

    return cart

if __name__ == "__main__":
    cart = Cart()
    apple = Product("apple", 0.5)
    bread = Product("bread", 6)
    water = Product("water", 2)
    orange = Product("orange", 1)

    print(input("Say hello: "))
    print("Good morning, we have apples, water, bread, and oranges. What do you need?")

    products = {"apple": apple, "bread": bread, "water": water, "orange": orange}
    cart = buy_products(cart, products)

    print("Here is your cart:")
    for product in cart.products:
        print(product.name)
##showing bill
    print("Here is your bill:")
    def generate_bill(cart):
        total_cost = 0
        print("Product Name\tPrice")
        for product in cart.products:
            print(f"{product.name}\t\t${product.price}")
            total_cost += product.price
        print(f"\nTotal cost: ${total_cost}")

    generate_bill(cart)