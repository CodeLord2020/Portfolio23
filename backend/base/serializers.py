from rest_framework import serializers

from .models import BlogPosts, Contact, MyProject, Tag


class MyProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProject
        fields = [
            "id",
            "title",
            "image",
            "description",
            "src_url",
            "project_url",
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    date = serializers.DateTimeField(source="created_at")
    lastmod = serializers.DateTimeField(source="updated_at")

    class Meta:
        model = BlogPosts
        fields = [
            "id",
            "title",
            "summary",
            "image",
            "content",
            "slug",
            "tags",
            "draft",
            "date",
            "lastmod",
        ]
