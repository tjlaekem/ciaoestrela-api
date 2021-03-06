# Generated by Django 3.0.3 on 2020-05-07 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.Model')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
            ],
            bases=('utils.model',),
        ),
    ]
