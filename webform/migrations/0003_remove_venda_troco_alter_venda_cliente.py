# Generated by Django 4.0 on 2022-11-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webform', '0002_venda_data_venda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='troco',
        ),
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.CharField(max_length=80),
        ),
    ]
