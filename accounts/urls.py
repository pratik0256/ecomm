from django.contrib import admin
from django.urls import path,include
from accounts.models import Cart
from accounts.views import login_page , register_page , activate_email  , add_to_cart , remove_cart , cart 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', login_page , name= "login"),
    path('register/', register_page, name='register_page'),
    # path('activate/<email_token/>', activate_email , name = "activate_email"),
    # # Corrected URL pattern
    path('activate/<email_token>/', activate_email, name="activate_email"),
    path('cart/' , cart , name="cart"),
    # path('cart/', cart_view, name='cart'),
    path('add-to-cart/<uid>/' , add_to_cart , name = "add_to_cart"),
    # path('remove-cart/<cart_item_uid>/' , remove_cart , name="remove_cart")
    path('remove-cart/<str:cart_item_uid>/', remove_cart, name='remove_cart')

    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)