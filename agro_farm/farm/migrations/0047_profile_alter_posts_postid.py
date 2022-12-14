# Generated by Django 4.1.3 on 2022-12-11 05:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0046_remove_reply_message_remove_reply_sent_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('gander', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('5f35979f-0349-40d6-b550-f46d8fd835db'), editable=False, primary_key=True, serialize=False),
        ),
    ]
