from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactUs
from django.shortcuts import render, redirect
from .forms import NewMessage
# Create your views here.

def contact_us(request):
    if request.method == 'GET':
        form = NewMessage()
    else:
        form = NewMessage(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            try:
                send_mail(subject, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, "contact_us.html", {'form': form})

def successView(request):
    return render(request, "success.html")
