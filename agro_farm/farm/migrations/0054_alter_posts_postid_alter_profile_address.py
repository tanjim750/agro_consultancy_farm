# Generated by Django 4.1.3 on 2022-12-11 09:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0053_alter_posts_postid_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('98a6eaa9-6a7a-42ac-81f9-52478281695d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
