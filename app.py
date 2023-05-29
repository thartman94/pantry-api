from config import app
from models import *


# from models import User
from config import db

# Blueprints
from user.user import (
    user,
)
from food_item.food_item import (
    food_item,
)

# idk how to do this better, is there an index.js type system for python?

app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(food_item, url_prefix="/food")


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        db.create_all()
