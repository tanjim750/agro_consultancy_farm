# Generated by Django 4.1.3 on 2022-12-07 13:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0043_alter_posts_postid_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='type',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('78dab69a-abe5-4793-85a3-bc56e100d26c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
