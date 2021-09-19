# Generated by Django 3.2.7 on 2021-09-18 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0010_delete_ienroll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='studentInClass',
            field=models.ManyToManyField(blank=True, related_name='studentInClass', to=settings.AUTH_USER_MODEL),
        ),
    ]
