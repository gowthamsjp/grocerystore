# Generated by Django 3.1.4 on 2021-04-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0027_auto_20210424_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fruits', 'Fruits'), ('Foods', 'Foods'), ('Bevarages', 'Beverages'), ('Others', 'Others'), ('Veggies', 'Veggies'), ('Indian', 'Indian'), ('Cookies', 'Cookies'), ('International', 'International'), ('Eggs', 'Eggs'), ('Dairy', 'Dairy'), ('Personal Care', 'Personal Care'), ('Detergents', 'Detergents')], default='Others', max_length=120),
        ),
    ]
