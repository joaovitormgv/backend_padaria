# Generated by Django 4.2.1 on 2024-01-18 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_padaria', '0007_cardapio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardapio',
            name='data_validade',
            field=models.DateField(blank=True, null=True, verbose_name='Data de validade'),
        ),
    ]
