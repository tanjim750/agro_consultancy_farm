# Generated by Django 4.1.3 on 2022-11-22 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0008_alter_addproducts_productid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproducts',
            name='productId',
            field=models.UUIDField(default=uuid.UUID('d80b560e-65cd-428e-9f8b-4a7b911df8e1'), editable=False, primary_key=True, serialize=False),
        ),
    ]
