# Generated by Django 3.0.4 on 2020-03-24 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoVenta',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('venta', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta')),
            ],
        ),
    ]