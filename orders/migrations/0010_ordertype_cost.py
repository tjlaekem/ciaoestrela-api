# Generated by Django 3.0.3 on 2020-02-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200213_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertype',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=6),
        ),
    ]
