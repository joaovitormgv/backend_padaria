# Generated by Django 4.2 on 2023-05-07 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_padaria', '0004_rename_clientes_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recebimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('data_emissao', models.DateField(auto_now_add=True, verbose_name='Data de Emissão')),
                ('data_vencimento', models.DateField(verbose_name='Data de Vencimento')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('pago', 'Pago'), ('cancelado', 'Cancelado')], max_length=30)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_padaria.cliente')),
            ],
        ),
    ]
