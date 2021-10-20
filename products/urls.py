from django.urls import path

from products.views import ProductListView, ProductDetailView, WishListListView, create_wishlist, add_to_cart

app_name = 'products'
urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('cart/<int:pk>/', add_to_cart, name='add-cart'),
    path('wishlist/', WishListListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', create_wishlist, name='create_wishlist'),
    path('', ProductListView.as_view(), name='list')
]