# Generated by Django 2.2 on 2020-03-23 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('precioTotal', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('tienda', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tienda.Tienda')),
            ],
        ),
    ]
