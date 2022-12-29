#importing models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
#Regular pizza model



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE )
    rsacard = models.CharField(max_length=15000, null=True, blank=True)

    def __str__(self):
        return f"{self.name.rsacard}"

class Regular_pizza(models.Model):
    name=models.CharField(max_length=64,primary_key=True)
    small=models.DecimalField(max_digits=4, decimal_places=2)
    large=models.DecimalField(max_digits=4,decimal_places=2)
    test=models.CharField(max_length=1000)
#Returns a string representation of any object
    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"
#Sicilian_pizza model     
class Sicilian_pizza(models.Model):
    name=models.CharField(max_length=64,primary_key=True)
    small=models.DecimalField(max_digits=4,decimal_places=2)
    large=models.DecimalField(max_digits=4,decimal_places=2)

#Returns a string representation of any object
    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"

# Topping model
class Topping(models.Model):
    name=models.CharField(max_length=64,primary_key=True)

#Returns a string representation of any object
    def __str__(self):
        return f"{self.name}"

#Sub model
class Sub(models.Model):
    name=models.CharField(max_length=64,primary_key=True)
    small=models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    large=models.DecimalField(max_digits=4,decimal_places=2)

#Returns a string representation of any object
    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"
#Pasta model
class Pasta(models.Model):
    name=models.CharField(max_length=64,primary_key=True)
    price=models.DecimalField(max_digits=4,decimal_places=2)

#Returns a string representation of any object
    def __str__(self):
        return f"{self.name} - {self.price}"

#Salad model
class Salad(models.Model):
    name=models.CharField(max_length=64,primary_key=True)
    price=models.DecimalField(max_digits=4,decimal_places=2)

#Returns a string representation of any object
    def __str__(self):
        return f"{self.name} - {self.price}"

#Dinner Platter model
class Dinner_platter(models.Model):
    name=models.CharField(max_length=64,primary_key=True)
    small=models.DecimalField(max_digits=4,decimal_places=2)
    large=models.DecimalField(max_digits=4,decimal_places=2)

#Returns a string representation of any object
    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"

#food model
class Food(models.Model):
    name=models.CharField(max_length=64,primary_key=True)

#Returns a string representation of any object
    def __str__(self):
        return f"{self.name}"

#User order model   
class User_order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_number=models.IntegerField()
    topping_allowance=models.IntegerField(default=0)
    status=models.CharField(max_length=64,default='initiated')
    
#Returns a string representation of any object
    def __str__(self):
        return f"{self.user} - {self.order_number} - {self.status} Topping_allowance: {self.topping_allowance}"

#Order price model
class Order_price(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    number=models.IntegerField()
    food=models.CharField(max_length=64,null=True)
    name=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    
#Returns a string representation of any object
    def __str__(self):
        return f"{self.name} - ${self.price} "

#Order counter model
class Order_counter(models.Model):
    counter=models.IntegerField()

#Returns a string representation of any object
    def __str__(self):
        return f"Order no: {self.counter}  "


from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

class Payment(models.Model):
    cc_number = CardNumberField(('card number'),primary_key=True)
    cc_expiry = CardExpiryField(('expiration date'))
    cc_code = SecurityCodeField(('security code'))
    amount=models.DecimalField(max_digits=10,decimal_places=2)


   