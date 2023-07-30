from cart import Cart
from product import Product

if __name__ == "__main__":
    cart = Cart()
    apple = Product("apple", 0.5)
    bread = Product("bread", 6)
    water = Product("water", 2)
    orange = Product("orange", 1)

##talk with shop worker
    print(input("say hello: "))
    print("good morning, we have apples, water, bread, and oranges. What do you need?")

##adding products to cart
    for i in range(3):
        product_name = input(f"What product do you need ({i + 1}/3): ").lower()
        if product_name == "apple":
            cart.products.append(apple)
            print("Added apple to your cart.")
        elif product_name == "bread":
            cart.products.append(bread)
            print("Added bread to your cart.")
        elif product_name == "water":
            cart.products.append(water)
            print("Added water to your cart.")
        elif product_name == "orange":
            cart.products.append(orange)
            print("Added orange to your cart.")
        else:
            print(f"Sorry, we don't have {product_name} in stock.")

    print("Here is your cart:")
    for product in cart.products:
        print(product.name)
        
##generating bill
    print("Here is your bill:")
    def generate_bill(cart):
        total_cost = 0
        print("Product Name\tPrice")
        for product in cart.products:
            print(f"{product.name}\t\t${product.price}")
            total_cost += product.price
        print(f"\nTotal cost: ${total_cost}")

    generate_bill(cart)