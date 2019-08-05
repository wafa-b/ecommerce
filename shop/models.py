from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='categories',on_delete=models.CASCADE)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse_lazy('product_list_by_category',args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE)
    description = models.TextField(max_length=4000,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/%Y/%m/%d',blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse_lazy('product_details',args=[self.slug])




