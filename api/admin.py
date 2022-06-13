from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Popularmodel, Recommendedmodel, usermodel,cartmodel,favmodel


@admin.register(Popularmodel)
class FoodAdmin(admin.ModelAdmin):
    list_display=['name','price','description','img','createdat','updatedat',id]


@admin.register(Recommendedmodel)
class FoodAdmin(admin.ModelAdmin):
    list_display=['name','price','description','img','createdat','updatedat',id]


@admin.register(usermodel)
class userAdmin(admin.ModelAdmin):
    list_display=['username','password','userid']


@admin.register(cartmodel)
class cartAdmin(admin.ModelAdmin):
    list_display=['productid','userid'] 


@admin.register(favmodel)
class favourites(admin.ModelAdmin):
    list_display=['productid','userid','isfav']
