from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                   help_text="percentage val")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
