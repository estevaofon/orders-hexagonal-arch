# Hexagonal Architecture Example in Python

This project demonstrates the implementation of the Hexagonal Architecture (also known as Ports and Adapters Pattern) in Python. It is designed to showcase how business logic can be decoupled from input/output mechanisms, facilitating easier testing and maintenance.

## Project Structure

The project is organized into four main directories:

- **domain**: Contains the core business logic and domain entities.
- **ports**: Defines interfaces (ports) for the external interactions with the application domain.
- **adapters**: Implements the ports with specific technologies or external interfaces.
- **application**: Contains the application setup and entry point.

## Implementation Details

- The Order and OrderService classes in domain/order.py represent the business logic.
- The OrderRepository interface in ports/repository.py is implemented by DatabaseAdapter in adapters/database.py, which simulates saving orders to a database.
- The main function in application/app.py initializes the necessary components and simulates an order transaction.

### Running the Application
```bash
python application/app.py
```