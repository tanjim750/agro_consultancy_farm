# Generated by Django 4.1.3 on 2022-11-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deletedSlogan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('slogan', models.TextField()),
                ('button1N', models.CharField(max_length=100)),
                ('button2N', models.CharField(max_length=100)),
                ('button1L', models.CharField(max_length=100)),
                ('button2L', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100)),
                ('brandName', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('banner1T', models.CharField(max_length=100)),
                ('banner1PD', models.CharField(max_length=100)),
                ('banner2T', models.CharField(max_length=100)),
                ('banner2PD', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sloganBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('slogan', models.TextField()),
                ('button1N', models.CharField(max_length=100)),
                ('button2N', models.CharField(max_length=100)),
                ('button1L', models.CharField(max_length=100)),
                ('button2L', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
