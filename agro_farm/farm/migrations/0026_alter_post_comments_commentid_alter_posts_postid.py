# Generated by Django 4.1.3 on 2022-11-24 13:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0025_alter_post_comments_commentid_alter_posts_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comments',
            name='commentId',
            field=models.UUIDField(default=uuid.UUID('14acfbf6-fbdd-4aaf-972e-c58d0446acf0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('8181b83c-da5a-4051-9e1e-19af277e1d59'), editable=False, primary_key=True, serialize=False),
        ),
    ]
