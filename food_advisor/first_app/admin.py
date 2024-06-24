from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.

class ProductPerson(admin.ModelAdmin):
    model = models.Person
    list_display = ['name', 'age', 'email', 'gender', 'phone_no','password']
class ProductAdvisor(admin.ModelAdmin):
    model = models.Advisor
    list_display = ['name', 'email', 'specification','password']
class ProductItem(admin.ModelAdmin):
    model = models.Item
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
    image_tag.short_description = 'Image'
    list_display = ['item_name', 'category', 'calories', 'vitamin', 'ingredient', 'image_tag']
class ProductReport(admin.ModelAdmin):
    model = models.Report
    list_display = ['date', 'total_calories','total_vitamins','consumed_items','total_ingredient' ]

class Advice_dis(admin.ModelAdmin):
    model = models.Advice
    list_display = ['advisor','description','item']
class Eaten_dis(admin.ModelAdmin):
    model = models.Eaten
    list_display = ['pr_name','item_id','date','quntity']
class Target_dis(admin.ModelAdmin):
    model = models.Target
    list_display = ['pr_nm', 'tr_calories', 'tr_vitamins']
admin.site.register(models.Advice,Advice_dis)



admin.site.register(models.Person,ProductPerson)
admin.site.register(models.Advisor,ProductAdvisor)
admin.site.register(models.Item,ProductItem)
admin.site.register(models.Report,ProductReport)
admin.site.register(models.Favorite_list)
admin.site.register(models.Eaten, Eaten_dis)
admin.site.register(models.Target, Target_dis)
admin.site.register(models.Feedback)



