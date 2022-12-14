# Generated by Django 4.1.3 on 2022-11-24 15:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0029_alter_post_comments_commentid_alter_posts_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comments',
            name='commentId',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('b21632c5-4869-47c3-bc84-2403d9cdc6a9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
