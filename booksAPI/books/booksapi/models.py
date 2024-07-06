from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Category Title')

    def __str__(self) -> str:
        return self.title

    
class Discounts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField()
    discount_percentage = models.DecimalField(max_digits=12, decimal_places=3)
    price = models.DecimalField(max_digits=12, decimal_places=3)

    def __str__(self) -> str:
        return self.title
    
class AirConditioner(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Brand')
    item_model = models.CharField(max_length=255, verbose_name='ItemModel')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return self.brand
    

class MobilePhones(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Brand')
    phone_model = models.CharField(max_length=255, verbose_name='PhoneModel')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return self.brand
    

class HouseholdAppliances(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Brand')
    appliance_model = models.CharField(max_length=255, verbose_name='ApplianceModel')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return self.brand


class Books(models.Model):
    author = models.CharField(max_length=255, verbose_name='Author')
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return self.title
    
class TV(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Brand')
    tv_model = models.CharField(max_length=255, verbose_name='TvModel')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return self.brand
    
class Laptops(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Brand')
    laptop_model = models.CharField(max_length=255, verbose_name='LaptopModel')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return self.brand