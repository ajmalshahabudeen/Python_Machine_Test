from django.db import models
from uuid import uuid4

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(max_length=255)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']
        

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateField(auto_now_add=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items'
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE
        )
    quantity = models.PositiveBigIntegerField()