
from django.shortcuts import redirect, render
from product.models import Product 
# Create your views here.



def get_products(request , slug ):
    
  
    try:
        print("Slug:", slug)
        product = Product.objects.get(slug = slug)
        context = {'product':product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            print(price)
            
        
        return render(request , 'product/product.html' , context= context )
    
    except Exception as e:
        print(e)


# from django.http import HttpResponseRedirect
# from .models import Product, Cart, CartItems, SizeVarient


