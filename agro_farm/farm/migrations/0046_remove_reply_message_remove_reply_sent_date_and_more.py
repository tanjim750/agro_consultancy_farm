# Generated by Django 4.1.3 on 2022-12-09 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farm', '0045_chat_seen_alter_posts_postid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='message',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='sent_date',
        ),
        migrations.AddField(
            model_name='reply',
            name='number_of_message',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('9dd70740-a923-4aae-a018-5d4f747ad5d9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
