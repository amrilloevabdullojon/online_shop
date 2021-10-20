from django.contrib import admin


# Register your models here.
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
