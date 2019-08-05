from django.shortcuts import render, get_object_or_404
from shop.models import Product
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def search(request):
    try:
        q = request.GET.get('q')

    except:
        None
    if q:
        products = Product.objects.filter(Q(name__icontains=q) | Q(category__name__icontains=q))

        paginator = Paginator(products, 8)
        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)


        return render(request, 'search.html', {'query':q,'products': products})

    else:
        return render(request, 'search.html', {})
