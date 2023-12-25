from django.db import models
from utils import validators


class Contact(models.Model):
    class Meta:
        db_table = "contacts"

    email = models.EmailField("Email Address", validators=[validators.email_regex])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} : {self.message[:20]}"

class NewsletterSubscriber(models.Model):
    class Meta:
        db_table = "news_letter_subscribers"

    email = models.EmailField(unique=True,validators=[validators.email_regex])
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

