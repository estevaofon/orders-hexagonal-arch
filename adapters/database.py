# adapters/database.py
from ports.repository import OrderRepository

class DatabaseAdapter(OrderRepository):
    def __init__(self):
        self.orders = []

    def save_order(self, order):
        print(f"Saving order to database: {order.description} for ${order.total}")
        self.orders.append(order)
