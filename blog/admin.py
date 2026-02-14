from django.contrib import admin
from blog.models import Post,category


class PostAdmin(admin.ModelAdmin):
     date_hierarchy = 'created_date'
     empty_value_display = '-empty-'
     list_display = ('title','author', 'created_date', 'status', 'published_date', 'counted_views')
     list_filter = ('status', 'published_date', 'author')
     search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(category)