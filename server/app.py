from flask import Flask
from flask_cors import CORS
import json

from utils.toJSON import toJSON
from model.User.User import User
from model.Product.Product import Product

people = toJSON([
    User("k@.ua", "John", "2323"),
    User("m@.ua", "Mike", "1241"),
    User("b@i.ua", "Bob", "1242"),
    User("d@i.ua", "Doe", "42112")
])

products = toJSON([
    Product("Ssamsung", "2000", )
])


print(people)

app = Flask(__name__)
CORS(app)


@app.route("/")
def users():
    return json.dumps(people)


# @app.route("/products")
# def users():
#     return


if __name__ == "__main__":
    app.run(port=3333)
