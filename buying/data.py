import json

def get_data():
    with open('buying/products.json') as f:
        return json.load(f)

