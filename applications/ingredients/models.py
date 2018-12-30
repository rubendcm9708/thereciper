from django.db import models

# Create your models here.
class Ingredient(models.Model):

    name = models.CharField('name', max_length=80, blank=False, null = False)

    MEASURE_CHOICES = (
        ('cl','centiliter'),
        ('lt','liter'),
        ('gr','gram'),
        ('kg','kilogram'),
    )

    measure = models.CharField('measure', choices = MEASURE_CHOICES, max_length=10, default='gr')

    quantity = models.DecimalField('quantity', max_digits=10, decimal_places=3, blank=False, null = False)

    price = models.DecimalField('price (€)', max_digits=10, decimal_places=2, blank=False, null = False)

    #article_number = models.IntegerField('article number', default=0)

    def __str__(self):
        return self.name
