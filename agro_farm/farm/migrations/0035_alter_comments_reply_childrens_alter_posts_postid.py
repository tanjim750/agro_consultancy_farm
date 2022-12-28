# Generated by Django 4.1.3 on 2022-11-26 10:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0034_rename_comment_comments_reply_reply_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_reply',
            name='childrens',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farm.comments_reply'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('23d1b0d8-503c-4b5b-97d5-45695769b198'), editable=False, primary_key=True, serialize=False),
        ),
    ]