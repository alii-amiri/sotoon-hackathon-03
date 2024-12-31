from django.contrib import admin
from core.models import Category, EmailTemplate
from users.models import CustomUser, Group


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'created_at', 'updated_at')
    search_fields = ('title',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    filter_horizontal = ('members',)  # For a better UI to select members

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title',)
    list_filter = ('category',)