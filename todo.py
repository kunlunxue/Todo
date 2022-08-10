import sqlite3
import argparse

the_conn = sqlite3.connect("./todoData.db")
# Declare the cursor in order to manipulate the database
the_cursor = the_conn.cursor()


# Create Todo class
class Todo:
    # The properties
    # todo id
    todo_id = ""
    # create time
    create_time = ""
    # total amount of all items
    total_amount = 0
    # amount of slashed items
    slashed_amount = 0
    # amount of standby items
    standby_amount = 0

    # Declare the connection of sqlite database

    def __init__(self):
        pass

    # Create and insert an Todo entity into the database
    def save_entity(self):
        the_cursor.execute("INSERT INTO Todo(TotalAmount) VALUES(1)")
        the_conn.commit()

    # Get Todo entity
    def get_entity(self, entity_id):
        pass

    # Get Todo entity
    def get_all_entity(self):
        the_cursor.execute("SELECT TodoID,TotalAmount FROM Todo")
        print(the_cursor.fetchall())

    # Get Items of one specified Todo entity
    def get_items(self, entity_id):
        pass

    # Complete the item,make a slash on the item
    def slash_item(self, entity_id, item_id):
        pass

    # Make the item standby, remove the slash on the item
    def standby_item(self, entity_id, item_id):
        pass

    # Add item to the Todo list
    def add_item(self, entity_id, item_id):
        pass

    # Remove item from the Todo List
    def remove_item(self, entity_id, item_id):
        pass

    # Rename the item
    def rename_item(self, entity_id, item_id):
        pass


# Create Item class
class Items:
    def __init__(self):
        pass

    # add item
    def add_item(self):
        pass

    # remove item
    def remove_item(self):
        pass

    # slash the item,it means complete it
    def slash_item(self):
        pass

    # make the item standby
    def standby_item(self):
        pass
