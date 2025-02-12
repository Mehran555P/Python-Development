products = [
    {"name": "Laptop", "price": 800, "quantity": 10},
    {"name": "Phone", "price": 500, "quantity": 15},
    {"name": "Headphones", "price": 50, "quantity": 30}
]

def add_product(name, price, quantity):
    new_product = {"name": name, "price": price, "quantity": quantity}
    products.append(new_product)
    print(f"Product {name} added successfully!")

def find_product(name):
    for product in products:
        if product["name"].lower() == name.lower():
            print(f"Product found: {product}")
            return
    print(f"Product with name '{name}' not found.")

def remove_product(name):
    for product in products:
        if product["name"].lower() == name.lower():
            products.remove(product)
            print(f"Product {name} removed successfully!")
            return
    print(f"Product with name '{name}' not found.")

def update_product(name, new_name, new_price, new_quantity):
    for product in products:
        if product["name"].lower() == name.lower():
            product["name"] = new_name
            product["price"] = new_price
            product["quantity"] = new_quantity
            print(f"Product {name} updated to: {product}")
            return
    print(f"Product with name '{name}' not found.")

add_product("Smartwatch", 150, 25)
find_product("Phone")
remove_product("Headphones")
update_product("Laptop", "Gaming Laptop", 1000, 8)

print("Final list of products:", products)
