from django.contrib import admin
from schedule import models

@admin.register(models.Contact )
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'email', 'phone_number',
    ordering = 'id',
    #list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 50
    list_max_show_all = 50
    #list_editable = 'first_name', 'last_name',
    list_display_links = 'id','first_name',