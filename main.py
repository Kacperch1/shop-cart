from cart import Cart
from product import Product
if __name__ == "__main__":
    cart = Cart()
    apple = Product("apple", 0.5)
    bread = Product("bread", 6)
    water = Product("water", 2)
    orange = Product("orange", 1)
## jak wygląda sklep?roduct
## 1.wchodzę witam się 2.mówię sprzedawcy co potrzebuję 3. gdy mam wszystko płace 4. pakuję to do siatki żegnam się i ide
    print(input("say hello: "))
    print("good morning, we have apples, water, bread and oranges. What do you need?")
    product1 = input("what product do you need: ")
    product2 = input("what second product do you need: ")
    product3 = input("what third product do you need: ")
    if product1.lower() == "apple":
        cart.products.append(apple)
        print("Added apple to your cart.")
    elif product1.lower() == "bread":
        cart.products.append(bread)
        print("Added bread to your cart.")
    elif product1.lower() == "water":
        cart.products.append(water)
        print("Added water to your cart.")
    elif product1.lower() == "orange":
        cart.products.append(orange)
        print("Added orange to your cart.")
    else:
        print(f"Sorry, we don't have {product1} in stock.")

    if product2.lower() == "apple":
        cart.products.append(apple)
        print("Added apple to your cart.")
    elif product2.lower() == "bread":
        cart.products.append(bread)
        print("Added bread to your cart.")
    elif product2.lower() == "water":
        cart.products.append(water)
        print("Added water to your cart.")
    elif product2.lower() == "orange":
        cart.products.append(orange)
        print("Added orange to your cart.")
    else:
        print(f"Sorry, we don't have {product2} in stock.")

    if product3.lower() == "apple":
        cart.products.append(apple)
        print("Added apple to your cart.")
    elif product3.lower() == "bread":
        cart.products.append(bread)
        print("Added bread to your cart.")
    elif product3.lower() == "water":
        cart.products.append(water)
        print("Added water to your cart.")
    elif product3.lower() == "orange":
        cart.products.append(orange)
        print("Added orange to your cart.")
    else:
        print(f"Sorry, we don't have {product3} in stock.")

    for Product in cart.products:
        print(Product.name)
##dokończyć
    print("here is you bill: ")
    def generate_bill(cart):
        total_cost = 0
        print("Product Name\tPrice")
        for product in cart.products:
            print(f"{product.name}\t\t${product.price}")
            total_cost += product.price
        print(f"\nTotal cost: ${total_cost}")
    generate_bill(cart)