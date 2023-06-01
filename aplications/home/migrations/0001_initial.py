# Generated by Django 4.2.1 on 2023-05-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='nombres')),
                ('pais', models.CharField(max_length=30, verbose_name='Pais')),
                ('pasaporte', models.CharField(max_length=50, verbose_name='Passaporte')),
                ('edad', models.IntegerField()),
                ('apelativo', models.CharField(max_length=10, verbose_name='Apelativo')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'persona',
            },
        ),
    ]
