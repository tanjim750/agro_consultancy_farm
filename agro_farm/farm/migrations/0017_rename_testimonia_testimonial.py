# Generated by Django 4.1.3 on 2022-11-23 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0016_alter_testimonia_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='testimonia',
            new_name='testimonial',
        ),
    ]