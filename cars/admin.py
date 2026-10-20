from django.contrib import admin
from cars.models import Car, State_numberCar,Comment_car, CategoryCar

admin.site.register(Car)
admin.site.register(State_numberCar)
admin.site.register(Comment_car)
admin.site.register(CategoryCar)