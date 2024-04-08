"""urls for appaira"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),      # URL for the home page
    path('cart/', views.cart, name='cart'),  # URL for the cart page
    path('cart/<Product_id>', views.addtocart, name='addtocart'),
    path('removefromcart/<Product_id>', views.removefromcart, name='removefromcart'),
    path('products/', views.products, name='products'),
    # Add other URLs here if needed
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('products/skincare/', views.skincare,name='skincare'),
    path('products/hair/', views.hair,name='hair'),
    path('products/makeup/', views.makeup,name='makeup'),
    path('products/fragrance/', views.fragrance,name='fragrance'),
    path('products/Bathnbody/', views.BathnBody, name = 'BathnBody'),
    path('products/Ordinary/', views.Ordinary, name = 'Ordinary',),
    path('products/cantu/', views.Cantu, name = 'Cantu',),
    path('products/charlotte/', views.Ordinary, name = 'Charlotte Tilbury',),
    path('products/esteelauder/', views.Ordinary, name = 'Estee Lauder',),
    path('products/fenty/', views.Ordinary, name = 'Fenty',),
    path('products/gisou/', views.Ordinary, name = 'Gisou',),
    path('products/mielle/', views.Ordinary, name = 'Mielle',),
    path('products/olaplex/', views.Ordinary, name = 'Olaplex',),
    path('products/rarebeauty/', views.Ordinary, name = 'Rare Beauty',),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
