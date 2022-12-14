# Generated by Django 4.1.3 on 2022-11-26 09:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0032_alter_posts_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postId',
            field=models.UUIDField(default=uuid.UUID('1252c72e-008b-4bb2-87fc-c099f3292303'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='comments_reply',
            fields=[
                ('replyId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='img/deafult.png', upload_to='img')),
                ('number', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('childrens', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='farm.comments_reply')),
                ('parent', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='farm.post_comments')),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.posts')),
            ],
        ),
    ]
