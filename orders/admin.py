
from django.contrib import admin
from .models import Regular_pizza, Sicilian_pizza, Topping, Sub, Pasta, Salad, Dinner_platter, Order_counter, Order_price, User_order, Food, Payment
# Register your models here.
#registering Regular Pizza model
admin.site.register(Regular_pizza)


admin.site.register(Sicilian_pizza)
#registering Sicilian pizza model
admin.site.register(Topping)
#registering Topping model
admin.site.register(Sub)
#registering Sub model
admin.site.register(Pasta)
#registering Pasta model
admin.site.register(Salad)
#registering Salad model
admin.site.register(Dinner_platter)
#registering Dinner platter 
admin.site.register(Food)
#registering Food model
admin.site.register(Order_counter)
#registering Order_counter model
admin.site.register(User_order)
#registering User_order model
admin.site.register(Order_price)
#registering Order_price model
admin.site.register(Payment)
#registering Order_price model