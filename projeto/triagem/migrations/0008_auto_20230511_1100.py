# Generated by Django 3.0.4 on 2023-05-11 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triagem', '0007_remove_triagem_data_nascimento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='triagem',
            options={'ordering': ['-data', '-hora', 'paciente2__nome'], 'verbose_name': 'triagem', 'verbose_name_plural': 'triagens'},
        ),
    ]
