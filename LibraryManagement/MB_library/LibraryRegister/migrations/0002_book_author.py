# Generated by Django 4.1.7 on 2023-02-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryRegister', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
