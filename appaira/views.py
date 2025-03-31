"""views for appaira"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .forms import AiraUserform
from .models import Product

def home(request):
    """home page for airapp"""
    return render(request, 'home.html')

@login_required
@csrf_protect
@require_POST
def add_to_cart_ajax(request, product_id):
    """Handle AJAX request to add item to cart"""
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False,
            'message': 'Please log in to add items to cart'
        }, status=401)

    try:
        product = get_object_or_404(Product, pk=product_id)
        
        # Check if product is already in cart
        if request.user not in product.cart.all():
            product.cart.add(request.user)
            cart_count = request.user.addtocart.count()
            return JsonResponse({
                'success': True,
                'message': 'Item added to cart successfully',
                'cart_count': cart_count
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Item is already in your cart'
            })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)

@login_required
def addtocart(request, Product_id):
    """Legacy cart addition for non-JS fallback"""
    if not request.user.is_authenticated:
        return redirect('login')

    product = get_object_or_404(Product, pk=Product_id)

    if request.user not in product.cart.all():
        product.cart.add(request.user)
    else:
        messages.error(request, "Error: You have already added this product to your cart.")
    
    # Return JSON response if it's an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': request.user.addtocart.count()
        })
    
    return redirect('cart')

def removefromcart(request, Product_id):
    """defining remove from cart"""
    product=get_object_or_404(Product,pk=Product_id)
    if request.user in product.cart.all():
        product.cart.remove(request.user)
        messages.success(request,'product remove from cart')
    return redirect('cart')

def register(request):
    """defining register to aira"""
    if request.method == 'POST':
        form = AiraUserform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            phone_number=form.cleaned_data.get('phone_number')
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            user=form.save(commit=False)
            user.email=email
            user.first_name=first_name
            user.last_name=last_name
            user.phone_number=phone_number
            user.save()
            user=authenticate(request,username=username, password=raw_password)
            return redirect('home')
    else:
        form = AiraUserform()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    """defining user login page"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Create the form
        if form.is_valid():  # Validate the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Authenticate user
            if user is not None:
                login(request, user)  # Log in the user
                return redirect('home')  # Redirect to the homepage or any other desired page
        else:
            print("Form errors: ", form.errors)
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()  # Create an empty form for GET requests

    context = {'form': form, 'is_logged_in': request.user.is_authenticated,
               'username': request.user.username if request.user.is_authenticated else None}
    return render(request, 'login.html', context)

def logout_view(request):
    """defining user logout page"""
    logout(request)
    return redirect('home')

def products(request):
    """show all products"""
    allproducts = Product.objects.all()
    return render(request,'products.html',{'products':allproducts})

def skincare(request):
    """adding skincare filter to products"""
    skincare_products = Product.objects.filter(category='Skincare')
    return render(request, 'skincare.html', {'skincare_products': skincare_products})

def hair(request):
    """adding haircare filter to products"""
    hair_products = Product.objects.filter(category="Hair")
    return render(request,'hair.html',{'hair_products': hair_products})

def makeup(request):
    """adding makeup filter to productSs"""
    makeup_products = Product.objects.filter(category="Makeup")
    return render(request,'makeup.html', {'makeup_products' : makeup_products})

def BathnBody(request):
    """adding bathnbody filter to products"""
    bathbody_products = Product.objects.filter(category="BathnBody")
    return render(request,'bathbody.html', {'bathbody_products' : bathbody_products})

def fragrance(request):
    """'adding fragrance filter to products"""
    fragrance_products = Product.objects.filter(category="Fragrance")
    return render(request,'fragrance.html', {'fragrance_products' : fragrance_products})

@login_required
def cart(request):
    """creating cart view"""
    cartview = request.user.addtocart.all()
    # Calculate cart total
    cart_total = sum(item.price for item in cartview)
    return render(request, 'cart.html', {
        'cart': cartview,
        'cart_total': format(cart_total, '.2f')
    })

def Mielle(request):
    """adding mielle brand filter to products"""
    mielle_products = Product.ojects.filter(brand="Mielle")
    return render(request, 'mielle.html', {'mielle_products' :  mielle_products})

def Ordinary(request):
    """adding ordinary brand filter to products"""
    ordinary_products = Product.objects.filter(brand="The Ordinary")
    return render(request, 'ordinary.html', {'ordinary_products' : ordinary_products})

def Fenty(request):
    """adding fenty brand filter to products"""
    fenty_products = Product.objects.filter(brand="Fenty Skin")
    return render(request, 'fenty.html', {'fenty_products' : fenty_products})

def Charlotte(request):
    """adding charlotte brand filter to products"""
    charlotte_products = Product.objects.filter(brand="Charlotte Tilbury")
    return render(request, 'charlotte.html', {'charlotte_products' : charlotte_products})

def Olaplex(request):
    """adding olaplex brand filter to products"""
    olaplex_products = Product.objects.filter(brand="Olaplex")
    return render(request, 'olaplex.html', {'olaplex_products' : olaplex_products})

def EsteeLauder(request):
    """adding esteelauder brand filter to products"""
    esteelauder_products = Product.objects.filter(brand="Estee Lauder")
    return render(request, 'esteelauder.html', {'esteelauder_products' : esteelauder_products})

def Gisou(request):
    """adding gisou brand filter to products"""
    gisou_products = Product.objects.filter(brand="Gisou")
    return render(request, 'gisou.html', {'gisou_products' : gisou_products})

def Rarebeauty(request):
    """adding rarebeauty brand filter to products"""
    rarebeauty_products = Product.objects.filter(brand="Rare Beauty")
    return render(request, 'rarebeauty.html', {'rarebeauty_products'  : rarebeauty_products})

def Cantu(request):
    """adding cantu brand filter to products"""
    cantu_products =Product.objects.filter(brand="Cantu")
    return render(request, 'cantu.html', {'cantu_products' : cantu_products})

def brand_view(request, brand_name):
    """View function for displaying products by brand"""
    # Create a mapping of URL-friendly names to actual brand names
    brand_mapping = {
        'ordinary': 'The Ordinary',
        'fenty': 'Fenty Skin',
        'charlotte': 'Charlotte Tilbury',
        'olaplex': 'Olaplex',
        'esteelauder': 'Estee Lauder',
        'gisou': 'Gisou',
        'mielle': 'Mielle',
        'rarebeauty': 'Rare Beauty',
        'cantu': 'Cantu'
    }
    
    # Get the actual brand name from the mapping, or use the provided name if not found
    actual_brand = brand_mapping.get(brand_name.lower(), brand_name)
    
    # Filter products by the brand
    brand_products = Product.objects.filter(brand=actual_brand)
    
    # Render the products template with the filtered products
    return render(request, 'products.html', {
        'products': brand_products,
        'brand_name': actual_brand
    })

@login_required
def update_cart(request, item_id, quantity):
    """Update cart item quantity and return new total"""
    try:
        # Get the product
        product = get_object_or_404(Product, pk=item_id)
        
        # Validate quantity
        if quantity < 1 or quantity > 10:
            return JsonResponse({
                'success': False,
                'error': 'Invalid quantity'
            })
        
        # Calculate new cart total
        cart_items = request.user.addtocart.all()
        cart_total = sum(item.price * (quantity if item.id == item_id else 1) for item in cart_items)
        
        return JsonResponse({
            'success': True,
            'cart_total': format(cart_total, '.2f')
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
    