# Generated by Django 4.1.7 on 2023-07-03 11:51

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.models.models_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(upload_to="authors/", verbose_name="Avatar"),
                ),
                (
                    "occupation",
                    models.TextField(
                        default="", max_length=500, verbose_name="Occupation"
                    ),
                ),
                (
                    "company",
                    models.CharField(default="", max_length=75, verbose_name="Company"),
                ),
                (
                    "twitter",
                    models.URLField(blank=True, null=True, verbose_name="Twitter"),
                ),
                (
                    "linkedin",
                    models.URLField(blank=True, null=True, verbose_name="Linkedin"),
                ),
                (
                    "github",
                    models.URLField(blank=True, null=True, verbose_name="Github"),
                ),
                (
                    "last_activity",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Last activity"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Email must be entered in the format: `abc@abc.com|net|org|info`.",
                                regex="^[A-z0-9\\.]+@[A-z0-9]+\\.(com|net|org|info)$",
                            )
                        ],
                        verbose_name="Email Address",
                    ),
                ),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "contacts",
            },
        ),
        migrations.CreateModel(
            name="DeviceTrack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_agent",
                    models.CharField(
                        blank=True,
                        help_text="e.g. Chrome 98, Windows, TECNO KE5, Android",
                        max_length=255,
                        null=True,
                        verbose_name="User Agent",
                    ),
                ),
                (
                    "user_device",
                    models.CharField(
                        choices=[
                            ("windows", "Windows"),
                            ("mac", "Mac"),
                            ("linux", "Linux"),
                            ("android", "Android"),
                            ("ios", "Ios"),
                            ("other", "Other"),
                        ],
                        max_length=12,
                    ),
                ),
                (
                    "ip_address",
                    models.GenericIPAddressField(
                        blank=True,
                        help_text="IP address of the device",
                        null=True,
                        verbose_name="IP Address",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        help_text="Location of the device",
                        max_length=255,
                        null=True,
                        verbose_name="Location",
                    ),
                ),
                (
                    "visited_data",
                    models.DateTimeField(
                        auto_now=True, help_text="The time when the user visit"
                    ),
                ),
            ],
            options={
                "verbose_name": "Device Activity",
                "verbose_name_plural": "Device Activity",
                "db_table": "device_track",
                "ordering": ("-visited_data",),
            },
        ),
        migrations.CreateModel(
            name="MyProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="default.jpg",
                        null=True,
                        upload_to=utils.models.models_fields.img_dir_path,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Required",
                        max_length=255,
                        unique=True,
                        verbose_name="Title",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        help_text="Not Required",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "src_url",
                    models.URLField(
                        blank=True,
                        help_text="Not Required",
                        null=True,
                        verbose_name="Source Code Url",
                    ),
                ),
                (
                    "project_url",
                    models.URLField(
                        blank=True,
                        help_text="Not Required",
                        null=True,
                        verbose_name="project_url",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
            ],
            options={
                "db_table": "my_projects",
            },
        ),
        migrations.CreateModel(
            name="NewsletterSubscriber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Email must be entered in the format: `abc@abc.com|net|org|info`.",
                                regex="^[A-z0-9\\.]+@[A-z0-9]+\\.(com|net|org|info)$",
                            )
                        ],
                    ),
                ),
                ("subscribed_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "news_letter_subscribers",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Required",
                        max_length=25,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
                "db_table": "tags",
            },
        ),
        migrations.CreateModel(
            name="BlogPosts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="default.jpg",
                        null=True,
                        upload_to=utils.models.models_fields.img_dir_path,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Required",
                        max_length=255,
                        unique=True,
                        verbose_name="Title",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("summary", models.TextField(max_length=500)),
                ("content", ckeditor.fields.RichTextField(verbose_name="Content")),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
                (
                    "draft",
                    models.BooleanField(
                        default=False, help_text="Draft post will not display"
                    ),
                ),
                ("author", models.ManyToManyField(to="base.author")),
                (
                    "tags",
                    models.ManyToManyField(related_name="post_tags", to="base.tag"),
                ),
            ],
            options={
                "verbose_name": "Blog Post",
                "verbose_name_plural": "Blog Posts",
                "db_table": "blog_post",
                "ordering": ("-updated_at", "-created_at"),
            },
        ),
    ]