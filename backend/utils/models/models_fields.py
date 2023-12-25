from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


def img_dir_path(instance, filename):
    return f"{instance.__class__.__name__}/{filename}"


class AbstractModel(models.Model):
    """Abstract base model for for all models."""

    class Meta:
        abstract = True

    image = models.ImageField(
        upload_to=img_dir_path,
        max_length=1000,
        default="https://res.cloudinary.com/dxs0fol71/image/upload/v1688536246/afe66629b25b6b778e46800144e13a7e_v9mnps.jpg",
    )
    title = models.CharField(
        "Title",
        help_text="Required",
        max_length=255,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
