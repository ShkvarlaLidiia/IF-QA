from model.Product.Product import Product
from utils.toJSON import toJSON

products = toJSON([
    Product("Samsung", 2000, "https://images.samsung.com/is/image/samsung/p6pim/ua/sm-a536elbdsek/gallery/ua-galaxy-a53-5g-a536-sm-a536elbdsek-531825969?$650_519_PNG$", "Smartphone"),
    Product("Samsung", 12000, "https://image-us.samsung.com/SamsungUS/home/televisions-and-home-theater/tvs/uhd-tv/tu8000/021020/gallery/PDP-GALLERY-TU8000-01-Front2-Titan-Gray-1600x1200.jpg?$product-details-jpg$", "TV"),
    Product("Samsung", 15000, "https://image-us.samsung.com/SamsungUS/home/home-appliances/refrigerators/06292022/rf27t5501sg/RF27T5501SG_01_BlackStainless_SCOM.jpg?$product-details-jpg$", "Fridge")
])
