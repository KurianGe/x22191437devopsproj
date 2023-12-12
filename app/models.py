from django.db import models
from django.contrib.auth.models import User

class BabysitterManager(models.Manager):
    def create_babysitter(self, model, price_per_hour, image):
        babysitter = self.model(model=model, price_per_hour=price_per_hour, image=image)
        babysitter.save()
        return babysitter

class Babysitter(models.Model):
    model = models.CharField(max_length=100)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='babysitter_images')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)
    
    objects = BabysitterManager()

    def __str__(self):
        return self.model
    
class CartItem(models.Model):
    babysitter = models.ForeignKey(Babysitter, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.babysitter.model}"
