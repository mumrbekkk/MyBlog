from django.contrib import admin
from .models import tag_model, author_model, post_model, comment_model


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class PostTagAdmin(admin.ModelAdmin):
    list_filter = ['author', 'tags', 'date']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'date', 'author']


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(tag_model.Tag, TagAdmin)
admin.site.register(author_model.Author, AuthorAdmin)
admin.site.register(post_model.Post, PostTagAdmin)
admin.site.register(comment_model.Comment, CommentAdmin)


# Super User: 1, 1@1.com, 1