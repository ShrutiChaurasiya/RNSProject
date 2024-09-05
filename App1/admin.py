from django.contrib import admin
from .models import * 
# Register your models 

@admin.register(Front)
class AdminDestination(admin.ModelAdmin):
    list_display=['id','bookname','book_desc','book_price','bookimage']


@admin.register(Buy)
class AdminDestination(admin.ModelAdmin):
    list_display=['id','accountname','bname','Branch','cvv','Email']

@admin.register(Purchase)
class AdminDestination(admin.ModelAdmin):
    list_display=['id','name','email','address','city','state','zip','cardName','cardNum']

@admin.register(Product)
class AdminDestination(admin.ModelAdmin):
    list_display=['id','bookname','author_name','book_desc','book_price','bookimage']

