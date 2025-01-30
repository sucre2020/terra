from db.dbconnection import db

products_collection = db["products"]

sample_products = [
    {
        "name": "Bees",
        "price": 20000,
        "description": "Healthy farm bees",
        "image": "/static/images/bees.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown", "White", "Black"],
    },
    {
        "name": "Bison",
        "price": 150000,
        "description": "Well-fed bison for farming/meat",
        "image": "/static/images/bison.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
    },
    {
        "name": "Bufalo",
        "price": 200000,
        "description": "Healthy bufalo for meat/farming",
        "image": "/static/images/bufalo.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown", "White", "Black"],
    },
    {
        "name": "Donkey",
        "price": 175000,
        "description": "Donkey for farming/etc",
        "image": "/static/images/donkey.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
    },
    {
        "name": "Duck",
        "price": "40000",
        "description": "Farm-bred duck",
        "image": "/static/images/ducks.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
    },
    {
        "name": "Geese",
        "price": "45000",
        "description": "Farm-bred geese",
        "image": "/static/images/geese.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
    },
    {
        "name": "Guinea Fowl",
        "price": "50000",
        "description": "Farm-bred guinea fowl",
        "image": "/static/images/guinea_fowl.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
    },
    {
        "name": "Guinea Pig",
        "price": "60000",
        "description": "Farm-bred guinea pig",
        "image": "/static/images/guinea_pigs.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
    },
    {
        "name": "Horses",
        "price": "400000",
        "description": "Farm-bred horse",
        "image": "/static/images/horses.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
    }
]

# Insert sample products only if the collection is empty
if products_collection.count_documents({})  < 100000:
    products_collection.insert_many(sample_products)
    print("Sample products added!")
else:
    print("Products already exist in the database.")
