# Generated by Django 5.0.4 on 2024-04-25 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantwatering', '0004_alter_plant_name_alter_plant_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
    ]
