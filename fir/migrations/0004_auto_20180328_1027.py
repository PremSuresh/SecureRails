# Generated by Django 2.0.3 on 2018-03-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0003_auto_20180328_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firstruc',
            old_name='latitute',
            new_name='latitude',
        ),
        migrations.AddField(
            model_name='firstruc',
            name='longitude',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
