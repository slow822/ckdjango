from django.contrib import admin
from .models import Watch

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price','description' ,'created_at','image')
    search_fields = ('name', 'brand')

# Register your models here.
