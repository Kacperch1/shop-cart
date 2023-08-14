from cart import Cart
class Shopping:
    @staticmethod
    def generate_bill(cart: Cart) -> None:
        total_cost: float = 0
        print("NPC: Product Name\tPrice\tQuantity\tTotal Price")

        for product, quantity in cart.products.items():
            print(f"  {product.name}\t${product.price:.2f}\t{quantity}\t\t${product.price * quantity:.2f}")
            total_cost += product.price * quantity

        print(f"NPC: Total cost: ${total_cost:.2f}")