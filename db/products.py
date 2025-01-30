from pymongo import ReturnDocument
from db.dbconnection import db

products_collection = db['products']

def create_product(name, price, description, image, gender_options, color_options):
    product_data = {
        "name": name,
        "price": price,
        "description": description,
        "image": image,
        "gender_options": gender_options,
        "color_options": color_options,
    }
    result = products_collection.insert_one(product_data)
    return result.inserted_id

def get_all_products():
    return list(products_collection.find())

def find_product_by_name(name):
    return products_collection.find_one({"name": name})

def update_product(name, updated_data):
    return products_collection.find_one_and_update(
        {'name': name},
        {"$set": updated_data},
        return_document=ReturnDocument.AFTER
    )

def delete_product(name):
    return products_collection.delete_one({"name": name}).deleted_count