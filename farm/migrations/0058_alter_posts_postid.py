# Generated by Django 4.1.4 on 2022-12-20 12:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0057_alter_posts_postid_orderedproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('46c3c9be-729c-42e1-beb7-ab4303900157'), editable=False, primary_key=True, serialize=False),
        ),
    ]
