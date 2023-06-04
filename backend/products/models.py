from django.db import models

 

from django.utils.translation import gettext_lazy as _ 
# Create your models here.
class Product(models.Model):
    title =models.CharField(_("title"), max_length=50)
    content = models.TextField(_("content"), max_length=50, blank=True, null= True)
    price = models.IntegerField(_("price"))

    @property
    def sale_price(self):
        return (self.price * 0.8)   

    def get_discount(self):
        return "900"