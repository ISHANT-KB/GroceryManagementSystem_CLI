import psycopg2
from db import connect


# add product to the innventory
def add_product(name, price, quantity):
    conn = connect()
    cur = conn.cursor()
    try: 
        cur.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", (name, price, quantity))
        conn.commit()
        print(f"product {name} added successfully.")
    except Exception as e:
        print("Error: ", e)
    finally:
        cur.close()
        conn.close()

# view inventory list
def view_products():
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM products ORDER BY id")
        rows = cur.fetchall()
        print("\nID | Name       | Price   | Quantity")
        print("-" * 40)
        for r in rows:
            # Convert price to float and quantity to int
            product_id = int(r[0])
            name = str(r[1])
            price = float(r[2])
            quantity = int(r[3])
            print(f"{product_id:<3}| {name:<10}| {price:<7.2f}| {quantity}")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# upadte the inventory product quantity
def update_product_quantity(product_id, new_quantity):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE products SET quantity = %s WHERE id = %s",
            (new_quantity, product_id)
        )
        if cur.rowcount == 0:
            print("No product found with that ID.")
        else:
            conn.commit()
            print(f"Product ID {product_id} updated successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

#delete the complete product row from the product table
def delete_product(product_id):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
        if cur.rowcount == 0:
            print("No product found with that ID.")
        else:
            conn.commit()
            print(f"Product ID {product_id} deleted successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

#search the product
def search_product(keyword):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM products WHERE name ILIKE %s", (f"%{keyword}%",))
        rows = cur.fetchall()
        if not rows:
            print("No products found.")
            return
        print("\nID | Name       | Price   | Quantity")
        print("-" * 40)
        for r in rows:
            product_id = int(r[0])
            name = str(r[1])
            price = float(r[2])
            quantity = int(r[3])
            print(f"{product_id:<3}| {name:<10}| {price:<7.2f}| {quantity}")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

#Total inventory
def total_inventory_value():
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT SUM(price * quantity) FROM products")
        total = cur.fetchone()[0] or 0
        print(f"Total Inventory Value: ₹{total:.2f}")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

#show low stock products
def low_stock_alert(threshold=5):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM products WHERE quantity <= %s ORDER BY quantity", (threshold,))
        rows = cur.fetchall()
        if not rows:
            print("No low-stock products.")
            return
        print("\nLow Stock Products:")
        print("ID | Name       | Price   | Quantity")
        print("-" * 40)
        for r in rows:
            print(f"{r[0]:<3}| {r[1]:<10}| {float(r[2]):<7.2f}| {int(r[3])}")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

#Main menu and beginning of the main program
def main_menu():
    while True:
        print("\n--- Grocery Management ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product Quantity")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Total Inventory Value")
        print("7. Low Stock Alert")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Product Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            add_product(name, price, quantity)
        elif choice == "2":
            view_products()
        elif choice == "3":
            product_id = int(input("Product ID to update: "))
            new_qty = int(input("New Quantity: "))
            update_product_quantity(product_id, new_qty)
        elif choice == "4":
            product_id = int(input("Product ID to delete: "))
            delete_product(product_id)
        elif choice == "5":
            keyword = input("Enter product name to search: ")
            search_product(keyword)
        elif choice == "6":
            total_inventory_value()
        elif choice == "7":
            threshold = int(input("Enter low-stock threshold: "))
            low_stock_alert(threshold)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


#start the projecct
if __name__ == "__main__":
    main_menu()