import sqlite3
import argparse


# Create Todo 类
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

    def __init__(self):
        pass

    # Get Todo entity
    def get_entity(self, entity_id):
        pass

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
