# Generated by Django 4.1.3 on 2022-11-22 16:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0007_addproducts_productimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproducts',
            name='productId',
            field=models.UUIDField(default=uuid.UUID('91b623c4-35a9-4d1e-906a-f7799344fbe4'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.addproducts'),
        ),
    ]