# Generated by Django 4.1.3 on 2022-11-26 17:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0038_alter_comments_reply_childrens_alter_posts_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_reply',
            name='childrens',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('43011b68-0d89-49cc-b956-f625d155550c'), editable=False, primary_key=True, serialize=False),
        ),
    ]