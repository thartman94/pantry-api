from config import app
from models import *


# from models import User
from config import db

# Blueprints
from user.user import (
    user,
)  # idk how to do this better, is there an index.js type system for python?
from inventory.inventory import inventory

app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(inventory, url_prefix="/inventory")


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        db.create_all()
