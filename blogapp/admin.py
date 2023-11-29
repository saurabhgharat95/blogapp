from django.contrib import admin
from .models import *

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ("title",)
    search_fields = ['title', 'author']
    list_per_page = 10

admin.site.register(UserProfile)
admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogComments)
admin.site.register(CategoryMaster)
admin.site.register(BlogCategory)
