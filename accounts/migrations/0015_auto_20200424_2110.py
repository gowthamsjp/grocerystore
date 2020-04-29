# Generated by Django 3.0.4 on 2020-04-25 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0014_auto_20200412_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='billing',
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='phone_number',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='state',
            field=localflavor.us.models.USStateField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserDefaultAddress',
        ),
    ]