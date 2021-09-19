# Generated by Django 3.2.7 on 2021-09-17 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sEnroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycourse', to='subjects.subject')),
            ],
        ),
    ]