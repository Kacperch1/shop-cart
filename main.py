from cart import Cart
from product import Product
from shopping import Shopping
from products import Products

if __name__ == "__main__":
    cart: Cart = Cart()

    print("NPC: Good morning! Welcome to our store. What can I assist you with today?")

    products: dict = {}
    for category_name in dir(Products):
        category = getattr(Products, category_name)
        if isinstance(category, type):
            for product_name, product_instance in category.__dict__.items():
                if isinstance(product_instance, Product):
                    products[product_name.lower()] = product_instance

    while True:
        action: str = input("What would you like to do? (shop/list/done): ").lower()

        if action == "done":
            break
        elif action == "list":
            print("Here is the list of available items:")
            for product_name in products:
                print(product_name)
        elif action == "shop":
            product_name: str = input("What product do you need (type 'done' to finish shopping): ").lower()
            if product_name == "done":
                break

            if product_name in products:
                product = products[product_name]
                quantity: int = int(input(f"How many {product_name}s do you want? "))
                cart.add_product(product, quantity)
                print(f"Added {quantity} {product_name}(s) to your cart.")
            else:
                print(f"NPC: I'm sorry, but we don't have {product_name} in stock.")
        else:
            print("NPC: I'm sorry, I didn't understand that.")

    print("Here is your cart:")
    for product, quantity in cart.products.items():
        if quantity > 1:
            print(f"{quantity} {product.name}s")
        else:
            print(product.name)

    print("Here is your bill:")

    Shopping.generate_bill(cart)