from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
products = [
    {"id": 1, "name": "Wireless Mouse", "description": "Ergonomic wireless mouse with long battery life", "quantity": 50, "price": 999},
    {"id": 2, "name": "Mechanical Keyboard", "description": "RGB backlit mechanical keyboard with blue switches", "quantity": 30, "price": 3499},
    {"id": 3, "name": "Gaming Headset", "description": "Surround sound gaming headset with noise cancellation", "quantity": 25, "price": 4999},
    {"id": 4, "name": "Laptop Stand", "description": "Adjustable aluminum laptop stand for better ergonomics", "quantity": 40, "price": 1499},
    {"id": 5, "name": "USB-C Hub", "description": "Multi-port USB-C hub with HDMI and Ethernet support", "quantity": 35, "price": 2799},
    {"id": 6, "name": "External Hard Drive", "description": "2TB portable external hard drive for backups", "quantity": 20, "price": 5999},
    {"id": 7, "name": "Wireless Earbuds", "description": "Bluetooth earbuds with noise cancellation and long battery", "quantity": 60, "price": 3999},
    {"id": 8, "name": "Smartwatch", "description": "Fitness smartwatch with heart rate and sleep monitoring", "quantity": 15, "price": 8999},
    {"id": 9, "name": "Portable Speaker", "description": "Waterproof Bluetooth speaker with deep bass", "quantity": 22, "price": 3499},
    {"id": 10, "name": "Webcam", "description": "Full HD webcam with built-in microphone", "quantity": 28, "price": 1999},
    {"id": 11, "name": "Smartphone Holder", "description": "Adjustable smartphone holder for desks and cars", "quantity": 70, "price": 699},
    {"id": 12, "name": "Graphic Tablet", "description": "Digital drawing tablet with pressure sensitivity", "quantity": 10, "price": 8999},
    {"id": 13, "name": "Wireless Charger", "description": "Fast wireless charger for all compatible devices", "quantity": 45, "price": 1299},
    {"id": 14, "name": "LED Ring Light", "description": "Dimmable LED ring light for video recording", "quantity": 32, "price": 2499},
    {"id": 15, "name": "VR Headset", "description": "Virtual reality headset with adjustable lenses", "quantity": 8, "price": 12999},
    {"id": 16, "name": "Portable SSD", "description": "1TB high-speed portable SSD for fast data transfer", "quantity": 18, "price": 7999},
    {"id": 17, "name": "Action Camera", "description": "4K action camera with waterproof case", "quantity": 12, "price": 10999},
    {"id": 18, "name": "Tripod Stand", "description": "Adjustable tripod stand for cameras and smartphones", "quantity": 40, "price": 1999},
    {"id": 19, "name": "Wireless Keyboard", "description": "Slim wireless keyboard with silent keys", "quantity": 25, "price": 1799},
    {"id": 20, "name": "Power Bank", "description": "20,000mAh power bank with fast charging support", "quantity": 50, "price": 2999},
]


def index(request):
    return render(request, "Pages/Homepage.html")

def product(request):

    return render(request,"Pages/Products.html", {"products" : products})

def ParticularProduct(request , Product_id):

    product_detail = ""

    id = Product_id
    for x in products:
        if x["id"] == id:
            product_detail = x

        # for y in x.keys():
        #     if y == "id":
        #         if x[y] == id:
        #             product_detail = x
        
    return render(request, "Pages/ParticularProduct.html", {"Product_id":id, "Product_detail":product_detail})

def Addtocart(request):
    return render(request, "Pages/AddtoCart.html")