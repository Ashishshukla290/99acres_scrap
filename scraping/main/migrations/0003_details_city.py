# Generated by Django 4.1.11 on 2023-09-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_details_property_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
