# Generated by Django 4.2.6 on 2023-11-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_usuarios_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='edad',
            field=models.IntegerField(default=0),
        ),
    ]