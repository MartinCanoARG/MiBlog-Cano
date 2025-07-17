from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'author', 'created_at')
    search_fields = ('title', 'subtitle', 'author__username')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)
