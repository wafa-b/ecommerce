from .models import Category,Product

def categories(request):
    categories = Category.objects.filter()
    return {'categories': categories}
