# Generated by Django 3.0.2 on 2021-01-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('Symptoms', models.CharField(max_length=300)),
                ('Description', models.CharField(max_length=1000)),
                ('Cause', models.CharField(max_length=500)),
            ],
        ),
    ]
