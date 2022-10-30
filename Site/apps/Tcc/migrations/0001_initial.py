# Generated by Django 4.1.2 on 2022-10-29 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(default=None, max_length=150)),
                ('titulo', models.CharField(default=None, max_length=150)),
                ('orientador', models.CharField(default=None, max_length=150)),
                ('ano_documento', models.IntegerField(default=None, verbose_name='Ano do Tcc')),
                ('resumo', models.TextField(default=None, max_length=150)),
            ],
        ),
    ]