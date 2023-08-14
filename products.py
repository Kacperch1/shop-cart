from product import Product

# todo introduce different product categories (i.e. Drinks, Meat, Wegetables, Fruits)
# todo Add them here and to the main logic


class Products:
    class Drinks:
        water: Product = Product("water", 2)
        soda: Product = Product("soda", 4)
        juice: Product = Product("juice", 3)

    class Meat:
        beef: Product = Product("beef", 7)
        lamb: Product = Product("lamb", 6)
        chicken: Product = Product("chicken", 4.5)
        steak: Product = Product("steak", 9)
        fish: Product = Product("fish", 5)

    class Vegetables:
        tomato: Product = Product("tomato", 1.5)
        onion: Product = Product("onion", 1.99)
        cucumber: Product = Product("cucumber", 0.9)
        carrot: Product = Product("carrot", 1.2)
        cabbage: Product = Product("cabbage", 2.7)
        broccoli: Product = Product("broccoli", 1.8)

    class Fruits:
        apple: Product = Product("apple", 0.5)
        orange: Product = Product("orange", 1)
        strawberry: Product = Product("strawberry", 1.99)
        grapes: Product = Product("grapes", 2.5)
        banana: Product = Product("banana", 0.8)
        pear: Product = Product("pear", 1.25)
        cherries: Product = Product("cherries", 3.25)

    class Dairy:
        milk: Product = Product("milk", 3.75)
        yoghurt: Product = Product("yoghurt", 2.8)
        cheese: Product = Product("cheese", 3.2)
        butter: Product = Product("butter", 1.3)

    class Bakery:
        bread: Product = Product("bread", 6)
        roll: Product = Product("roll", 0.75)
        bagel: Product = Product("bagel", 1.2)
        baguette: Product = Product("baguette", 2)

