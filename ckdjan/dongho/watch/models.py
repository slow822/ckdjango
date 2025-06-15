from django.db import models

# Create your models here.

class Watch(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='static/assets/', null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name