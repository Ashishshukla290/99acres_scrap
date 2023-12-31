# Generated by Django 4.1.11 on 2023-09-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=300)),
                ('property_cost', models.CharField(max_length=50)),
                ('property_type', models.CharField(max_length=300)),
                ('property_area', models.CharField(max_length=50)),
                ('property_link', models.URLField(max_length=300)),
            ],
        ),
    ]
