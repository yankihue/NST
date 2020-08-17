from django.contrib import admin
from .models import Question,Post,Comment
# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    fields= ['title','link','tags']
    inlines = [CommentInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Post,PostAdmin)