# Generated by Django 3.0.5 on 2023-09-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_details_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
