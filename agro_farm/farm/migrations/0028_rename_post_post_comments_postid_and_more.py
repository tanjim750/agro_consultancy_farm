# Generated by Django 4.1.3 on 2022-11-24 13:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0027_alter_post_comments_commentid_alter_posts_postid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_comments',
            old_name='post',
            new_name='postId',
        ),
        migrations.AlterField(
            model_name='post_comments',
            name='commentId',
            field=models.UUIDField(default=uuid.UUID('fa3c8cf4-5602-4769-929f-3a20325a99e9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('0f681ece-de5b-4ad8-8f1a-82579d9fdd32'), editable=False, primary_key=True, serialize=False),
        ),
    ]
