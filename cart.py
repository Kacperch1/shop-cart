class Cart:
    def __init__(self):
        self.products: dict = {}

    def add_product(self, product: str, quantity: int) -> None:
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity