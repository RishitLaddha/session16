# Inventory System Assignment

[![Python application](https://github.com/RishitLaddha/session16/actions/workflows/python-app.yml/badge.svg)](https://github.com/RishitLaddha/session16/actions/workflows/python-app.yml) 

<img width="1222" alt="Screenshot 2025-02-18 at 19 54 00" src="https://github.com/user-attachments/assets/6fed86d6-900a-4a13-a3fe-a462e066891c" />


## Overview

This repository contains an inventory management system built in Python, primarily focusing on the creation and manipulation of dictionaries. 

- **inventory_system.py**: This is the main module containing functions for inventory management. The module includes functions to create an inventory, update inventory details, merge multiple inventories, view categories and items, and perform both deep and shallow copying.


## Key Learning Objectives

This assignment emphasizes several critical areas in Python programming:

1. **Creating Python Dictionaries**:
    - **Methods**: We demonstrated multiple methods for creating dictionaries, including the use of the `dict()` constructor and dictionary comprehensions. This shows that dictionaries in Python are flexible and can be instantiated in several ways.
    - **Practical Example**: In our inventory system, the 'Electronics' category is created using the `dict()` constructor, ensuring that the keys are exactly as required (e.g., "Laptop", "Smartphone"). On the other hand, the 'Groceries' category is built using a dictionary comprehension which iterates over a list of product details.

2. **Common Operations on Dictionaries**:
    - **Updating**: The `update_inventory` function highlights how to modify existing dictionary entries using the `update()` method. This is crucial in many applications where the state of an object needs to be dynamically altered.
    - **Merging**: The `merge_inventories` function combines two inventories into one. It carefully handles cases where items are present in both inventories by summing their quantities and ensuring that the highest price is retained.
    - **Copying**: Through the `copy_inventory` function, we differentiate between deep and shallow copying, which is essential when dealing with nested data structures. Deep copying creates an entirely independent copy of the data, while shallow copying maintains references to the original objects.

3. **Dictionary Views**:
    - **Dynamic Nature**: The functions `view_categories` and `view_category_item_pairs` showcase how dictionary views work in Python. These views provide a dynamic reflection of the dictionary's keys and key-value pairs, meaning they update automatically when the dictionary changes.
    - **Utility**: The `view_all_items` function uses a list comprehension to extract all item details from nested dictionaries, converting the data into a flat list that is easier to iterate over or manipulate further.

4. **Custom Classes and Hashing**:
    - **Hashable Keys**: In Python, dictionaries rely on hashing to store keys. This assignment reinforces that dictionary keys must be hashable. While our example uses simple immutable types (strings) as keys, it introduces the fundamental concept that if you ever need to use a custom object as a key, the object must implement the `__hash__()` and `__eq__()` methods.
    - **Extensibility**: Although the current implementation does not include custom classes, understanding hashing is critical for students who plan to extend the project. For instance, you might create a custom class to represent products, but you would need to ensure that instances of this class are hashable if they are to be used as dictionary keys.

## Detailed Walkthrough of the Code

### `create_inventory()`

This function is the starting point of our inventory system. It demonstrates two distinct methods of dictionary creation:

- **dict() Constructor**: Used to create the 'Electronics' category, it ensures that the items like "Laptop" and "Smartphone" are stored with precise key names.
- **Dictionary Comprehension**: Employed for the 'Groceries' category, it iterates over a predefined list of tuples, where each tuple contains the product name, price, and quantity.

The careful construction of these dictionaries is critical because several subsequent functions rely on the presence of specific keys and values (e.g., "Laptop" in "Electronics", "Apple" in "Groceries").

### `update_inventory()`

The `update_inventory` function is responsible for modifying the details of an existing item in the inventory. It checks if both the category and the item exist before applying the update. This function is a practical demonstration of how the `update()` method can be used to alter nested dictionaries efficiently.

### `merge_inventories()`

One of the more complex operations demonstrated in this project is merging two inventory systems. The function starts by making a deep copy of the first inventory to ensure that any modifications do not affect the original data. It then iterates over the second inventory, merging data by:
- Adding new categories if they don’t exist.
- For overlapping items, summing the quantities and ensuring that the item’s price is updated to the highest value.

This function illustrates the importance of deep copying in Python, especially when working with nested structures, and shows how multiple data sources can be integrated seamlessly.

### `get_items_in_category()`

A simple but effective utility function, `get_items_in_category`, retrieves all items from a given category. It leverages the dictionary’s `get()` method, which provides a safe way to access values without risking a KeyError if the category is missing. This pattern is common in many real-world applications where data integrity and fault tolerance are important.

### `find_most_expensive_item()`

This function iterates over all items in the inventory to determine which one has the highest price. It showcases how to traverse nested dictionaries and perform comparisons, making it a useful example of iterative data processing in Python.

### `check_item_in_stock()`

The `check_item_in_stock` function searches across all categories for a specific item. It returns the item’s details if found or `None` otherwise. This function is particularly relevant in scenarios where checking the availability of a product is essential.

### `view_categories()` and `view_category_item_pairs()`

These functions illustrate the dynamic nature of dictionary views. `view_categories` returns the keys (i.e., category names) of the inventory, while `view_category_item_pairs` returns a view of the entire dictionary as (key, value) pairs. Both functions demonstrate how dictionary views can be utilized to quickly inspect and iterate over dictionary contents.

### `view_all_items()`

To facilitate the easy retrieval of all products in the inventory, `view_all_items` uses a list comprehension that flattens the nested dictionaries into a single list of item details. This operation is particularly useful for reporting or data analysis purposes.

### `copy_inventory()`

Finally, `copy_inventory` shows the difference between deep and shallow copying. Deep copies duplicate all nested objects, ensuring complete independence from the original data, while shallow copies only duplicate the outer dictionary. This distinction is crucial in scenarios where the inventory may be modified independently of its source.

## Conclusion

By exploring the functions provided in `inventory_system.py`, one can gain valuable insights into:

- Multiple methods of dictionary creation.
- The importance of updating and merging operations in data management.
- How to use dictionary views to inspect and manipulate data.
- The fundamental concept of hashing and its relevance to using custom classes as dictionary keys.




