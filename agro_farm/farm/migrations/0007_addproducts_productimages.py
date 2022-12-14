# Generated by Django 4.1.3 on 2022-11-22 16:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0006_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='addproducts',
            fields=[
                ('productId', models.UUIDField(default=uuid.UUID('6008922f-15c4-447b-84d0-4526a3bbb01f'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('price', models.TextField()),
                ('offerPrice', models.TextField()),
                ('rating', models.TextField()),
                ('offerParsentage', models.CharField(max_length=100)),
                ('delivey_Time', models.CharField(max_length=100)),
                ('certificate', models.TextField()),
                ('description', models.TextField()),
                ('efectiveness', models.TextField()),
                ('star1', models.IntegerField(default=0)),
                ('star2', models.IntegerField(default=0)),
                ('star3', models.IntegerField(default=0)),
                ('star4', models.IntegerField(default=0)),
                ('star5', models.IntegerField(default=0)),
                ('reviews', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='productimages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('product_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='farm.addproducts')),
            ],
        ),
    ]
