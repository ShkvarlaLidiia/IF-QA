from flask import Flask
from flask_cors import CORS


from connection import connection

app = Flask(__name__)
CORS(app)


def get_data():
    data = connection()

    data_collection = data['users']

    return data_collection.find()


@app.route("/")
def home():
    data = get_data()

    users = []

    for doc in data:
        doc['_id'] = str(doc["_id"])
        users.append(doc)

    return users


if __name__ == "__main__":
    app.run(port=3333)
