# Generated by Django 3.0.4 on 2020-04-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='no_of_stud',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='placement',
            name='package',
            field=models.IntegerField(default=0),
        ),
    ]