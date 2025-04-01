from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="home"),
    path("product", views.product, name="product" ),
    path("add-to-cart", views.Addtocart, name="add-to-cart"),
    path("Product/Selected-Product/<int:Product_id>", views.ParticularProduct, name="ParticularProduct"),
]