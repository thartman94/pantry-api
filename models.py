from config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date)
    inventories = db.relationship("Inventory", backref="user", lazy=True)

    def __init__(self, first_name, last_name, email, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_joined = date_joined


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    food_items = db.relationship("Inventory", backref="food_item", lazy=True)

    def __init__(self, user_id, name, description):
        self.user_id = user_id
        self.name = name
        self.description = description


class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.Column(db.Integer, db.ForeignKey("food_item.id"), nullable=False)
    name = db.Column(db.String(100))
    size_grams = db.Column(db.Integer)
    serving_size_grams = db.Column(db.Integer)
    fat_grams = db.Column(db.Integer)
    protien_grams = db.Column(db.Integer)
    carbs_grams = db.Column(db.Integer)
    exp_date = db.Column(db.Date)

    def __init__(
        self,
        inventory_id,
        name,
        size_grams,
        serving_size_grams,
        fat_grams,
        protien_grams,
        carbs_grams,
        exp_date,
    ):
        self.inventory_id = inventory_id
        self.name = name
        self.size_grams = size_grams
        self.serving_size_grams = serving_size_grams
        self.fat_grams = fat_grams
        self.protien_grams = protien_grams
        self.carbs_grams = carbs_grams
        self.exp_date = exp_date
