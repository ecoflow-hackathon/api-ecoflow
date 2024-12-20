# Generated by Django 5.1.3 on 2024-11-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('is_admin', models.BooleanField(default=False)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True)),
            ],
        ),
    ]
