# Generated by Django 4.1.3 on 2022-12-07 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farm', '0041_chat_room_chat_user_alter_posts_postid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='room',
        ),
        migrations.AlterField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('e4c69c8c-f527-479c-a0b9-4a9e20afbc5b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
