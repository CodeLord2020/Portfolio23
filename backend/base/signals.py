from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import loader

from .models import BlogPosts, Contact, NewsletterSubscriber


@receiver(post_save, sender=Contact)
def contact_signals(sender, instance, created, **kwargs):
    if created:
        template = loader.get_template("contact-email.html")
        subject = "My Portfolio"
        message = template.render({"contact": instance})
        email = EmailMessage(
            subject,
            message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.RECIPIENT_ADDRESS],
        )
        email.send()


@receiver(post_save, sender=BlogPosts)
def blog_signals(sender, instance, created, **kwargs):
    if created:
        subscribers = NewsletterSubscriber.objects.all()

        template = loader.get_template("blog-post-email.html")
        subject = "Check My New Post!"
        message = template.render({"post": instance})

        for subscriber in subscribers:
            email = EmailMessage(
                subject,
                message,
                from_email=settings.EMAIL_HOST_USER,
                to=[subscriber.email],
            )
            email.send()
