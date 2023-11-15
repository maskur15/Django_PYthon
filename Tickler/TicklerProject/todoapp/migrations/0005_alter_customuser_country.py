# Generated by Django 4.2.5 on 2023-10-24 13:18

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_customuser_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(default='Bangladesh', max_length=2),
        ),
    ]
