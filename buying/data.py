import json

def get_data():
    """
        Get products list from json file
        args:
        return []products
    """
    with open('buying/products.json') as f:
        return json.load(f)

