# Generated by Django 4.1.3 on 2022-11-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0013_alter_addproducts_productid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='img')),
                ('top_title', models.CharField(max_length=100)),
                ('button_1_name', models.CharField(max_length=100)),
                ('button_2_name', models.CharField(max_length=100)),
                ('button_1_link', models.CharField(max_length=100)),
                ('button_2_link', models.CharField(max_length=100)),
                ('contact_box_text', models.CharField(max_length=100)),
                ('contact_box_title', models.CharField(max_length=100)),
                ('conTi', models.CharField(max_length=100)),
                ('location_title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email_title', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number_title', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
            ],
        ),
    ]
