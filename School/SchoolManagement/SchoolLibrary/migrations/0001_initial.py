# Generated by Django 4.1.7 on 2023-02-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=110)),
                ('author', models.CharField(max_length=111)),
                ('book_link', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
