# Generated by Django 4.2.7 on 2024-01-10 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myBlogDdDefined',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostName', models.CharField(max_length=100)),
                ('PostContent', models.CharField(max_length=10000000)),
                ('TimeCreated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
