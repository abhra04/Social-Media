# Generated by Django 3.1 on 2020-12-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_person_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='unique_id',
            field=models.IntegerField(default=0),
        ),
    ]