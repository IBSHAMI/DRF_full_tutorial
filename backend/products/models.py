from django.db import models

class Product(models.Model): 
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.PositiveBigIntegerField(default=19.99)
    
