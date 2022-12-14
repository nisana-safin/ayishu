from django.contrib import admin



# Register your models here.


from shop.models import category, products
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(category,catadmin)
class prodadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','image']
    list_editable = ['price',  'image']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(products,prodadmin)
