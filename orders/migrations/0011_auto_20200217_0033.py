# Generated by Django 3.0.3 on 2020-02-17 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_ordertype_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customcard',
            name='ideas',
            field=models.TextField(blank=True),
        ),
    ]
