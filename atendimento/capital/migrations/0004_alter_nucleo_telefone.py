# Generated by Django 5.1 on 2024-09-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capital', '0003_alter_nucleo_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nucleo',
            name='telefone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
