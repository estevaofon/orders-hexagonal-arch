# application/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from domain.order import OrderService
from adapters.database import DatabaseAdapter


def main():
    repository = DatabaseAdapter()
    order_service = OrderService(repository)

    # Simulating placing an order
    order = order_service.place_order("Book", 29.99)
    print(f"Order placed: {order.description} for ${order.total}")


if __name__ == "__main__":
    main()