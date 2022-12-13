# Generated by Django 4.1.3 on 2022-12-11 06:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0050_profile_image_alter_posts_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('c2f54523-15e2-428d-b94b-7b60e59df050'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]