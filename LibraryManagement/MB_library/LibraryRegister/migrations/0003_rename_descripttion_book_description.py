# Generated by Django 4.1.7 on 2023-02-20 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryRegister', '0002_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='descripttion',
            new_name='description',
        ),
    ]
