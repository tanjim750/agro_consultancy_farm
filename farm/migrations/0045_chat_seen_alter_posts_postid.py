# Generated by Django 4.1.3 on 2022-12-08 09:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0044_chat_type_alter_posts_postid'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='seen',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('e3ef00c3-fce8-4ea3-9cf3-3349dbe4243b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
