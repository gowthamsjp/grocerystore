# Generated by Django 3.0.4 on 2020-03-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_remove_product_timestamps'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamps',
            field=models.DateTimeField(auto_now=True),
        ),
    ]