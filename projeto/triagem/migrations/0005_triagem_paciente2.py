# Generated by Django 3.0.4 on 2023-05-04 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('triagem', '0004_auto_20230420_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='triagem',
            name='paciente2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paciente2', to='paciente.Paciente', verbose_name='Paciente *'),
        ),
    ]
