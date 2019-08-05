from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category,Product

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm

from django.db.models import Count
from orders.models import OrderItem

# Create your views here.
def index(request):

    top_orders = OrderItem.objects.annotate(Count('product')).order_by('-product__count')[:3]

    categories = Category.objects.all()

    # products = Product.objects.all()

    products = Product.objects.order_by('-created_at')


    page = request.GET.get('page', 1)

    paginator = Paginator(products, 8)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    cart_product_form = CartAddProductForm()

    return render(request,'home.html',{'top_orders':top_orders,'categories':categories,'products':products,'cart_product_form':cart_product_form})

def product_list_by_category(request,slug):

    category = get_object_or_404(Category,slug=slug)

    products = Product.objects.filter(category=category)

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 4)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    cart_product_form = CartAddProductForm()


    return render(request,'product_list_by_category.html',{'category':category,'products':products,'cart_product_form':cart_product_form})


def product_details(request,slug):

    product = get_object_or_404(Product,slug=slug)

    cart_product_form = CartAddProductForm()

    return render(request,'product_details.html',{'product':product,'cart_product_form':cart_product_form})


