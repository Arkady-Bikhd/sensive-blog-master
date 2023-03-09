from django.contrib import admin
from .models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text',)
    raw_id_fields = ('likes', 'tags',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post',)
    raw_id_fields = ('author',)


admin.site.register(Tag)