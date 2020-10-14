from django.contrib import admin
from .models import Movie , UserProfile, Plans
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
        'genre',
        'views'
    ]
    list_filter = ['genre']
    search_fields = ['name']

admin.site.register(Plans,PlansAdmin)
admin.site.register(Movie,MoveAdmin)
admin.site.register(UserProfile,UserProfileAdmin)