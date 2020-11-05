from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':['name']}

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'slug', 'synopsis', 'director', 'released_date', 'created_date']
    list_filter = ['category', 'released_date', 'created_date']
    prepopulated_fields = {'slug':('title',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)

