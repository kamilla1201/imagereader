from django.contrib import admin
from .models import Post
from .models import Source

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date')
	list_display_links = ('id', 'title')

class SourceAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'link')
	list_display_links = ('id', 'user')

admin.site.register(Post, PostAdmin)
admin.site.register(Source, SourceAdmin)
# Register your models here.
