# Generated by Django 3.0.4 on 2020-04-28 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0017_auto_20200422_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mainImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]