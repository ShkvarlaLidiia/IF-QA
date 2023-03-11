from flask import Flask,  jsonify, request
from flask_cors import CORS

from utils.toJSON import toJSON
from model.User.User import User
from model.Product.Product import Product

users = toJSON([
    User("k@.ua", "John", "2323"),
])


app = Flask(__name__)
CORS(app)

# * ROUTES


def getData(arr):
    return arr


@app.route("/")
def home():
    return "<h2>Server works!</h2>"


@app.route("/products")
def products():
    print(request.method)
    return jsonify(toJSON([
        Product(
            "Bitcoin",
            "$22451.89",
            "https://static.vecteezy.com/system/resources/previews/008/822/064/original/3d-design-bitcoin-cryptocurrency-white-background-free-png.png",
            "A cryptocurrency is a digital currency, which is an alternative form of payment created using encryption algorithms. The use of encryption technologies means that cryptocurrencies function both as a currency and as a virtual accounting system."
        ),
        Product(
            "Ethereum",
            "$1571.36",
            "https://www.logo.wine/a/logo/Ethereum/Ethereum-Icon-Purple-Logo.wine.svg",
            "A cryptocurrency is a digital currency, which is an alternative form of payment created using encryption algorithms. The use of encryption technologies means that cryptocurrencies function both as a currency and as a virtual accounting system."
        ),
        Product(
            "ZSU Coin",
            "$1.00",
            "https://upload.wikimedia.org/wikipedia/commons/9/9a/%D0%95%D0%BC%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0_%D0%97%D0%A1%D0%A3.png",
            "A cryptocurrency is a digital currency, which is an alternative form of payment created using encryption algorithms. The use of encryption technologies means that cryptocurrencies function both as a currency and as a virtual accounting system."
        ),
        Product(
            "BNB",
            "$451.89",
            "https://upload.wikimedia.org/wikipedia/commons/9/9a/%D0%95%D0%BC%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0_%D0%97%D0%A1%D0%A3.png",
            "A cryptocurrency is a digital currency, which is an alternative form of payment created using encryption algorithms. The use of encryption technologies means that cryptocurrencies function both as a currency and as a virtual accounting system."
        ),
        Product(
            "Dogecoin",
            "$213.89",
            "https://cryptologos.cc/logos/dogecoin-doge-logo.png",
            "A cryptocurrency is a digital currency, which is an alternative form of payment created using encryption algorithms. The use of encryption technologies means that cryptocurrencies function both as a currency and as a virtual accounting system."
        ),
        Product(
            "Solana",
            "$21.25",
            "https://cryptologos.cc/logos/solana-sol-logo.png",
            "A cryptocurrency is a digital currency, which is an alternative form of payment created using encryption algorithms. The use of encryption technologies means that cryptocurrencies function both as a currency and as a virtual accounting system."
        ),
    ])
    )

# @app.route("/products")
# def users():
#     return "Hello"


if __name__ == "__main__":
    app.run(port=3333)
