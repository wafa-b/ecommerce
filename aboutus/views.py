from django.shortcuts import render, get_object_or_404

from .models import AboutUs

# Create your views here.
def about_us(request):

    aboutus = AboutUs.objects.all()

    return render(request,'about_us.html',{'aboutus':aboutus})
