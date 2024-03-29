# Generated by Django 4.1.7 on 2023-03-17 11:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created',
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated',
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('demo_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('source_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('vote_total', models.IntegerField(default=0)),
                ('vote_ratio', models.FloatField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('tags', models.ManyToManyField(blank=True, to='journal_app.tag')),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='journal_app.projects'),
        ),
        migrations.DeleteModel(
            name='Papers',
        ),
    ]
