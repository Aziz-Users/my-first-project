from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', SingleProductView.as_view()),
    path('images/', ProductImageListCreate.as_view()),
    path('catagory/', CategoryListCreate.as_view()),
    path('cart/', CartListCreate.as_view()),
    path('cart/delete/<int:product_id>/', CartView.as_view()),
    path('products/<str:category_slug>/',ProductListByCategoryView.as_view()),
    path('categories/',CategoryListCreate.as_view())
]
