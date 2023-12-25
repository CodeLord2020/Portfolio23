from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from utils.models.models_fields import AbstractModel


class Tag(models.Model):
    class Meta:
        """Meta options for the model"""

        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        db_table = "tags"

    name = models.CharField(
        "Name",
        help_text="Required",
        max_length=25,
        unique=True,
    )
    slug = models.SlugField(
        "Slug",
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


class BlogPosts(AbstractModel):
    class Meta:
        """Meta options for the model"""

        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        db_table = "blog_post"
        ordering = ("-updated_at", "-created_at")

    summary = models.TextField(max_length=500)
    content = RichTextField(
        "Content",
    )
    tags = models.ManyToManyField(Tag, related_name="post_tags")
    slug = models.SlugField(
        "Slug",
        unique=True,
    )
    draft = models.BooleanField(
        default=False,
        help_text="Draft post will not display",
    )

    @property
    def blog_link(self):
        return settings.BLOG_URL + "/blog/" + self.slug

    def __str__(self):
        return f"{self.title}: {self.summary[:30]}"
