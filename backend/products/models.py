from django.db import models

class Product(models.Model): 
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(default=19)
    
    @property
    def discount_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_price_plus_vat(self):
        return "%.2f" %(float(self.price) * 1.2)
    
    @property
    def sale_price(self):
        # discount 2 decimal places
        return "{:.2f}".format(self.price * 0.9)
    
    def get_discount(self):
        return "100"
    
    
    
