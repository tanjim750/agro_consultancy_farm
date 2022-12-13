from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from .models import profile
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail

#For Send html template to email
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string

def create_profile(sender, instance  , created , **kwargs):
    if created:
        info = profile(user=instance)
        info.save()

        subject = 'welcome to Agro Consultancy Farm'
        #message = f'<h1>Email from Agro Consultancy Farm </h1><br>Hi {instance},<br> Thank you for registering in Agro Consultancy Farm.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email, ]
        # send_mail(subject, message, email_from, recipient_list)

        html_template = render_to_string('welcome.html',{'username':instance.username, 'email':instance.email, 'title':subject})
        message = strip_tags(html_template)

        email = EmailMultiAlternatives(
                subject,
                message,
                email_from,
                recipient_list
        )
        email.attach_alternative(html_template, 'text/html')
        email.send()


post_save.connect(create_profile, sender=User)



