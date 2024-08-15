# Generated by Django 5.1 on 2024-08-08 18:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('codigoArt', models.CharField(max_length=100)),
                ('nombreArt', models.CharField(max_length=100)),
                ('descripcionArt', models.CharField(max_length=100)),
                ('unidadBaseArt', models.CharField(max_length=100)),
                ('unidadSatArt', models.CharField(max_length=100)),
                ('claveSatArt', models.CharField(max_length=100)),
                ('precioArt', models.DecimalField(decimal_places=20, default=0.0, max_digits=32, null=True)),
            ],
            options={
                'ordering': ('codigoArt',),
            },
        ),
    ]