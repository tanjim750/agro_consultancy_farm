# Generated by Django 4.1.3 on 2022-12-11 05:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0049_alter_posts_postid_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/img/deafult.png', upload_to='img'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('8f1ab2ea-63bd-4fb8-811e-f0964fedde8e'), editable=False, primary_key=True, serialize=False),
        ),
    ]