from django.contrib import admin

from .models import BlogPosts, Contact, MyProject, NewsletterSubscriber, Tag

admin.site.register(Contact)
admin.site.register(NewsletterSubscriber)


@admin.register(MyProject)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
    ]
    list_filter = ["is_active"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
    ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BlogPosts)
class BlogPostsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "draft",
        "created_at",
        "updated_at",
    ]
    list_filter = ["draft", "title"]
    prepopulated_fields = {"slug": ("title",)}
