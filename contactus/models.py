from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=400)
    message = models.TextField(max_length=5000)
    email = models.EmailField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

