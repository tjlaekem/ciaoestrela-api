# Generated by Django 3.0.3 on 2020-05-18 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.Model')),
                ('url', models.URLField(blank=True)),
            ],
            bases=('utils.model',),
        ),
        migrations.AlterField(
            model_name='pin',
            name='image_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
