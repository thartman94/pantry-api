from config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date)

    def __init__(self, first_name, last_name, email, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_joined = date_joined


class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    size = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    serving_size = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    protien = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    exp_date = db.Column(db.Date)

    def __init__(
        self,
        name,
        brand,
        size,
        serving_size,
        calories,
        fat,
        protien,
        carbs,
        exp_date,
    ):
        self.name = name
        self.brand = brand
        self.size = size
        self.serving_size = serving_size
        self.calories = calories
        self.fat = fat
        self.protien = protien
        self.carbs = carbs
        self.exp_date = exp_date
