# Generated by Django 3.0.4 on 2023-04-20 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicamento',
            options={'ordering': ['-is_active', 'tarja', 'nome_real'], 'verbose_name': 'medicamento', 'verbose_name_plural': 'medicamentos'},
        ),
        migrations.AlterModelManagers(
            name='medicamento',
            managers=[
            ],
        ),
    ]
