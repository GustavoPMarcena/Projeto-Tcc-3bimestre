# Generated by Django 4.1.2 on 2022-10-29 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tcc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcc',
            name='arquivo',
            field=models.FileField(default=None, upload_to='uploads/'),
        ),
    ]