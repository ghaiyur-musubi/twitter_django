# Generated by Django 3.1.2 on 2020-11-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image_path',
            field=models.CharField(max_length=280, null=True),
        ),
    ]
