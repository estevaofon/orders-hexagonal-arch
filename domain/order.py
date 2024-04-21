# domain/order.py
class Order:
    def __init__(self, description, total):
        self.description = description
        self.total = total

class OrderService:
    def __init__(self, repository):
        self.repository = repository

    def place_order(self, description, total):
        order = Order(description, total)
        self.repository.save_order(order)
        return order