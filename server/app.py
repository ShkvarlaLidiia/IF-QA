from flask import Flask
from flask_cors import CORS
import json

from model.database.People import people
from model.database.Products import products

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
