# Generated by Django 4.0.3 on 2022-04-10 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothingStore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quantity',
            new_name='days',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='pricePerDay',
        ),
    ]
