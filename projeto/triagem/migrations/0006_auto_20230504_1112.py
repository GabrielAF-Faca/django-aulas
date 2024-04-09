# Generated by Django 3.0.4 on 2023-05-04 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('triagem', '0005_triagem_paciente2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='triagem',
            options={'ordering': ['-data', '-hora', 'paciente2__nome'], 'verbose_name': 'triagem', 'verbose_name_plural': 'triagenss'},
        ),
        migrations.AlterUniqueTogether(
            name='triagem',
            unique_together={('data', 'hora', 'paciente2')},
        ),
        migrations.RemoveField(
            model_name='triagem',
            name='paciente',
        ),
    ]
