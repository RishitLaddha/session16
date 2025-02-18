"""
inventory_system.py

This module provides a simple inventory management system using Python dictionaries.
It demonstrates various dictionary operations including creation, updating, merging,
viewing, and copying. The code is designed as an educational tool to illustrate
the power and versatility of Python dictionaries, as well as to introduce some
concepts related to custom classes and hashing.
"""

import copy

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and the dict() constructor.
    
    The inventory contains two main categories:
      - 'Electronics': created using the dict() constructor.
      - 'Groceries': created using a dictionary comprehension.
    
    Additional products have been added to each category while ensuring that the
    expected items (e.g., 'Laptop' in 'Electronics' and 'Apple' in 'Groceries')
    remain unchanged to satisfy external test requirements.
    
    Returns:
        dict: An inventory dictionary with categories as keys and dictionaries
              of items as values.
    """
    # Creating the 'Electronics' category using the dict() constructor
    electronics = dict(
        Laptop={"name": "Laptop", "price": 1000, "quantity": 5},
        Smartphone={"name": "Smartphone", "price": 800, "quantity": 10},
        Smartwatch={"name": "Smartwatch", "price": 300, "quantity": 20}  # Additional product
    )
    
    # Creating the 'Groceries' category using a dictionary comprehension.
    # Each tuple in the list represents (item_name, price, quantity).
    grocery_data = [
        ("Apple", 1, 50),
        ("Banana", 0.5, 100),
        ("Orange", 2, 30)  # Additional product
    ]
    groceries = {
        item: {"name": item, "price": price, "quantity": quantity}
        for item, price, quantity in grocery_data
    }
    
    # Combine the categories into the final inventory dictionary.
    inventory = {"Electronics": electronics, "Groceries": groceries}
    return inventory

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., price or quantity) in the inventory.
    
    Parameters:
        inventory (dict): The inventory dictionary.
        category (str): The category in which the item exists.
        item_name (str): The name of the item to update.
        update_info (dict): A dictionary containing update information (e.g., {'price': 1200}).
    
    If the specified category and item exist, the function updates the item using the update() method.
    """
    if category in inventory and item_name in inventory[category]:
        inventory[category][item_name].update(update_info)

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    
    Parameters:
        inv1 (dict): The first inventory dictionary.
        inv2 (dict): The second inventory dictionary.
    
    The function creates a deep copy of inv1 and then iterates through inv2. If a category or item
    exists in both inventories, it sums the quantities and updates the price to the maximum value.
    If a category or item is only present in inv2, it is added to the merged inventory.
    
    Returns:
        dict: A merged inventory dictionary.
    """
    merged = copy.deepcopy(inv1)
    for category, items in inv2.items():
        if category not in merged:
            # Use deep copy to avoid linking to the original objects.
            merged[category] = copy.deepcopy(items)
        else:
            for item, details in items.items():
                if item in merged[category]:
                    # Sum the quantities and update the price to the maximum value.
                    merged[category][item]["quantity"] += details["quantity"]
                    merged[category][item]["price"] = max(
                        merged[category][item]["price"], details["price"]
                    )
                else:
                    merged[category][item] = details
    return merged

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    
    Parameters:
        inventory (dict): The inventory dictionary.
        category (str): The category to retrieve items from.
    
    Returns:
        dict: A dictionary of items in the given category. Returns an empty dictionary if the category is not found.
    """
    return inventory.get(category, {})

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    
    Parameters:
        inventory (dict): The inventory dictionary.
    
    Returns:
        dict or None: The details of the most expensive item if found, otherwise None.
    
    The function iterates through all items across all categories and compares their prices.
    """
    max_price = 0
    most_expensive = None
    for category in inventory.values():
        for item in category.values():
            if item["price"] > max_price:
                max_price = item["price"]
                most_expensive = item
    return most_expensive

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    
    Parameters:
        inventory (dict): The inventory dictionary.
        item_name (str): The name of the item to check.
    
    Returns:
        dict or None: The details of the item if found; otherwise, None.
    
    The function searches each category for the given item name.
    """
    for category in inventory.values():
        if item_name in category:
            return category[item_name]
    return None

def view_categories(inventory):
    """
    View available categories (the keys of the outer dictionary).
    
    Parameters:
        inventory (dict): The inventory dictionary.
    
    Returns:
        dict_keys: A view object displaying the categories.
    """
    return inventory.keys()

def view_all_items(inventory):
    """
    Retrieve all items across all categories.
    
    Parameters:
        inventory (dict): The inventory dictionary.
    
    Returns:
        list: A list of dictionaries, each containing details of an item.
    
    This function uses a list comprehension to iterate over every category and item.
    """
    return [details for category in inventory.values() for details in category.values()]

def view_category_item_pairs(inventory):
    """
    View category-item pairs as dictionary items.
    
    Parameters:
        inventory (dict): The inventory dictionary.
    
    Returns:
        dict_items: A view object of (category, items) pairs.
    """
    return inventory.items()

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure.
    
    Parameters:
        inventory (dict): The inventory dictionary.
        deep (bool): If True, returns a deep copy; if False, returns a shallow copy.
    
    Returns:
        dict: A copy of the inventory dictionary.
    
    A deep copy duplicates all nested dictionaries, ensuring that modifications to the copy do not affect the original.
    A shallow copy creates a new dictionary with references to the original nested objects.
    """
    return copy.deepcopy(inventory) if deep else inventory.copy()

# End of inventory_system.py
