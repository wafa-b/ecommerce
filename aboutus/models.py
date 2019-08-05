from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    subject = models.TextField(max_length=4000)

    def __str__(self):
        return self.title
