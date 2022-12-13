# Generated by Django 4.1.3 on 2022-12-11 09:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0052_rename_gander_profile_gender_alter_posts_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('3c62d9ac-b23e-4b9d-be6b-9a1d7e325462'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
