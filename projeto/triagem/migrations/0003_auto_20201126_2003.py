# Generated by Django 3.0.4 on 2020-11-26 23:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triagem', '0002_auto_20201126_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triagem',
            name='altura',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(2.5)], verbose_name='Altura em metros *'),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(400.0)], verbose_name='Peso em kg *'),
        ),
    ]
