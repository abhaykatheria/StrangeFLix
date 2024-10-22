from django.contrib import admin
from .models import Movie , UserProfile, Plans, Payment, Comment
# Register your models here.

class PlansAdmin(admin.ModelAdmin):
    list_display = ['plan_type' , 'plan_price', 'plan_length']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'is_active_plan',
    ]
    list_filter = ['is_active_plan']
    search_fields = ['user']

class MoveAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'prime_show',
        'genre',
        'views',
        'imdb',
        'director',
        'year',
        'actors',
    ]
    list_filter = ['genre','prime_show']
    search_fields = ['name']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','amount','timestamp']
    list_filter = ['amount']
    search_fields = ['user']

admin.site.register(Plans,PlansAdmin)
admin.site.register(Movie,MoveAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Payment,PaymentAdmin)