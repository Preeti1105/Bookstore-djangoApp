# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('books/', views.book_list, name='book_list'),
#     path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/', views.cart_view, name='cart'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('books/', views.book_list, name='book_list'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('logout/', views.user_logout, name='logout'),
]
