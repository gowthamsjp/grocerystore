# Generated by Django 3.0.4 on 2020-04-12 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200412_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdefaultaddress',
            name='billing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_default_billing_address', to='accounts.UserAddress'),
        ),
        migrations.AlterField(
            model_name='userdefaultaddress',
            name='shipping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_default_address', to='accounts.UserAddress'),
        ),
    ]