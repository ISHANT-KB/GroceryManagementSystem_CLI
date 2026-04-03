# Grocery Management System (GMS CLI)

A command-line interface application for managing grocery inventory using PostgreSQL database.

## Features

- Add new products to inventory
- View all products in inventory
- Update product quantities
- Delete products from inventory
- Search products by name
- Calculate total inventory value
- Low stock alerts with customizable threshold

## Requirements

- Python 3.x
- PostgreSQL database
- psycopg2 library

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd GMS_cli
   ```

2. Install dependencies:

   ```bash
   pip install psycopg2-binary
   ```

3. Set up PostgreSQL database:
   - Create a database named `grocery_db`
   - Create a table named `products` with the following schema:
     ```sql
     CREATE TABLE products (
         id SERIAL PRIMARY KEY,
         name VARCHAR(100) NOT NULL,
         price DECIMAL(10,2) NOT NULL,
         quantity INTEGER NOT NULL
     );
     ```

4. Update database credentials in `db.py` if necessary:
   - Default settings: user='postgres', password='19682007', host='localhost', port='5432'

## Usage

Run the application:

```bash
python grocery.py
```

The application will display a menu with the following options:

1. Add Product - Add a new product to inventory
2. View Products - Display all products in inventory
3. Update Product Quantity - Modify quantity of existing product
4. Delete Product - Remove a product from inventory
5. Search Product - Find products by name (case-insensitive)
6. Total Inventory Value - Calculate total value of all inventory
7. Low Stock Alert - Show products below specified quantity threshold
8. Exit - Quit the application

## Database Connection

The application connects to PostgreSQL using the credentials specified in `db.py`. Make sure your PostgreSQL server is running and the database exists before running the application.

## Files

- `db.py` - Database connection module
- `grocery.py` - Main application with CLI interface
- `README.md` - This file

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is open source and available under the MIT License.
