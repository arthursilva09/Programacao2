# Generated by Django 4.0 on 2022-11-10 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='data_venda',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
