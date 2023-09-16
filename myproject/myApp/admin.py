from django.contrib import admin
from .models import *
# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_display=['image','name','description']
admin.site.register(GalleryModel,GalleryAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display=['name','email','Phonenumber','address']
admin.site.register(RegisterModel,RegisterAdmin)

    
class GalAdmin(admin.ModelAdmin):
    list_display=['gallery','name','product_image']
admin.site.register(Product,GalAdmin)

    
