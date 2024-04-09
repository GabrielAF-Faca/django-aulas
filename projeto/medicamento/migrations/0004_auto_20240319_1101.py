# Generated by Django 3.0.4 on 2024-03-19 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0001_initial'),
        ('medicamento', '0003_medicamento_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='fornecedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fornecedor', to='fornecedor.Fornecedor', verbose_name='Fabricante do medicamento'),
        ),
    ]
