# Generated by Django 5.0.6 on 2024-05-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client', models.TextField(max_length=255)),
                ('value', models.FloatField()),
            ],
        ),
    ]
