from ckeditor.fields import RichTextField
from django.db import models
from utils.models.models_fields import AbstractModel


class MyProject(AbstractModel):
    class Meta:
        db_table = "my_projects"
    
    description = RichTextField(
        "Description",
        help_text="Not Required",
        null=True,
        blank=True,
    )
    src_url = models.URLField(
        "Source Code Url",
        help_text="Not Required",
        blank=True,
        null=True,
    )
    project_url = models.URLField(
        "project_url",
        help_text="Not Required",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField("Is Active", default=True)

    def __str__(self):
        return self.title
